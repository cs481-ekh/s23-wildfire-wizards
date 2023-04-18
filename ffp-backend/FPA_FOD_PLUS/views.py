from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from django.db.models import Q
from django.shortcuts import render
import csv
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import os
import subprocess
import time

from .models import Data
from .helpers import addAllCategories, categoryHelper, defaultFields, postalToState, stateList

all_query_params = ['LATITUDE', 'LONGITUDE','FIRE_SIZE','FIRE_SIZE__gte','FIRE_SIZE__lte','FIRE_SIZE__range','FIRE_YEAR','FIRE_YEAR__gte',
                    'FIRE_YEAR__lte','FIRE_YEAR__range', 'DISCOVERY_DATE','DISCOVERY_DATE__gte','DISCOVERY_DATE__lte','DISCOVERY_DATE__range',
                    'DISCOVERY_DOY','DISCOVERY_DOY__gte','DISCOVERY_DOY__lte','DISCOVERY_DOY__range', 'DISCOVERY_TIME','DISCOVERY_TIME__gte',
                    'DISCOVERY_TIME__lte','DISCOVERY_TIME__range', 'CONT_DATE','CONT_DATE__gte','CONT_DATE__lte','CONT_DATE__range', 'CONT_DOY',
                    'CONT_DOY__gte','CONT_DOY__lte','CONT_DOY__range','CONT_TIME','CONT_TIME__gte','CONT_TIME__lte','CONT_TIME__range', 'STATE',
                    'COUNTY','Ecoregion_US_L4CODE', 'Ecoregion_US_L3CODE', 'Ecoregion_NA_L3CODE', 'Ecoregion_NA_L2CODE','Ecoregion_NA_L1CODE',
                    'NWCG_CAUSE_CLASSIFICATION']

def index(request):
    return HttpResponse("Hello, world. You're at the FPA-FOD-Plus index page.")
    
# @api_view(['GET'])
# def heat_map(request):
#     if request.method == 'GET':
#         # limit to august fires 
#         data = Data.objects.filter(
#             FIRE_YEAR=2018,
#             # DISCOVERY_DOY__lte=243,
#             # DISCOVERY_DOY__gte=100,
#             FIRE_SIZE__gte=1,
#         # Filter out any broken latitude / longitude fields
#         ).exclude(
#             LATITUDE=0
#         ).exclude(
#             LONGITUDE=0
#         ).values('LATITUDE', 'LONGITUDE', 'FIRE_SIZE')

#         serializer = HeatMapSerializer(data, context={'request': request}, many=True)

#         return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# helper function to remove filter option before use in .values()
def remove_filter(string):
    filters = ["__gte", "__lte", "__range"]
    for f in filters:
        string = string.replace(f, '')
    return string

# helper function to grab low and high ranges from string formated as such "low-high"
def format_ranges(map):    
    for key in map:
        if "__range" in key:
            map[key] = map[key].split('->')
    return map

# todo: discovery date, CONT_DATE, needs to be reformatted? or stored differently?

@api_view(['GET'])
def perform_search(request):
    if request.method == 'GET':
        requested_fields = {}
        # grab query params
        for p in all_query_params:
            # if we have a value for field as param
            # then add to requested_fields
            value = request.query_params.get(p,None)
            if value:
                if p == 'COUNTY':
                    p = 'LatLong_County'
                requested_fields[p] = value

        requested_fields = format_ranges(requested_fields)

        # always return values for latitude, longitude, and fire size to be able to map
        columns = list(map(lambda s: remove_filter(s), requested_fields.keys()))
        columns.append("LATITUDE")
        columns.append("LONGITUDE")
        columns.append("FIRE_NAME")
        columns.append("FOD_ID")
        columns.append("FPA_ID")
        columns.append("NWCG_CAUSE_CLASSIFICATION")
        
        # still return these values if not requested
        if "DISCOVERY_DATE" not in columns:
            columns.append("DISCOVERY_DATE")
        if "CONT_DATE" not in columns:
            columns.append("CONT_DATE")
        if "FIRE_SIZE" not in columns:
            columns.append("FIRE_SIZE")

        # now construct queryset using requested_fields dictionary
        queryset = Data.objects.filter(**requested_fields).values(*columns).order_by('FIRE_SIZE')
        serializer = searchSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def subset_csv(request):
    if request.method == 'GET':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'

        requested_fields = {}
        # grab query params
        for p in all_query_params:
            # if we have a value for field as param
            # then add to requested_fields
            value = request.query_params.get(p,None)
            if value:
                if p == 'COUNTY':
                    p = 'LatLong_County'
                requested_fields[p] = value

        #get categories param and turn it into list
        categories = request.query_params.get('CATEGORIES',None)
        if(categories!=None):
            categories = categories.split(',')

        requested_fields = format_ranges(requested_fields)

        #add FOD_ID no matter what
        fields_list = categoryHelper(categories)
        for f in defaultFields():
            if f not in fields_list:
                fields_list.insert(0, f)
            else:
                fields_list.remove(f)
                fields_list.insert(0, f)

        # now construct queryset using requested_fields dictionary
        queryset = Data.objects.filter(**requested_fields).values(*fields_list).order_by('FOD_ID')
        serializer = FireRecordSerializer(queryset, context={'request': request}, many=True)
        
        header = fields_list

        fire_data = serializer.data
        fields_to_remove = []

        for row in fire_data:
            for key in row:
                if key not in fields_list:
                    fields_to_remove.append(key)
            for key in fields_to_remove:
                row.pop(key, None)

        #header = [f.name for f in Data._meta.fields]
        #header = FireRecordSerializer.Meta.fields

        writer = csv.DictWriter(response, fieldnames=header)
        writer.writeheader()
        for row in fire_data:
            writer.writerow(row)

    return response
    #return Response(response.content)


@api_view(['GET'])
def fire_by_id(request):
    if request.method == 'GET':
        id = request.query_params.get("FOD_ID",None)

        # now construct queryset using id
        queryset = Data.objects.filter(FOD_ID = id).all()
        serializer = FireRecordSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def variable_list(request):
    if request.method == 'GET':
        serializer = VariableListSerializer()
        return Response(serializer.data)
  
@api_view(['GET'])
def distinct_years_list(request):
    if request.method == 'GET':
        serializer = DistinctYearsSerializer()
        return Response(serializer.data)

@api_view(['GET'])
def distinct_states_list(request):
    if request.method == 'GET':
        return Response(stateList())

def results(request):
    query_results = Data.objects.filter(NWCG_REPORTING_UNIT_ID='USCACDF')
    response = ""
    for row in query_results:
        response += "FOD_ID: " + str(row.FOD_ID)
        response += " FPA_ID: " + str(row.FPA_ID)
        response += " NAME: " + str(row.NAME) + "\n"
    
    return HttpResponse(response)
    
@api_view(['GET'])
def distinct_counties_list(request):
    if request.method == 'GET':
        state = request.query_params.get('STATE')
        state = postalToState(state)
        fetched_counties = Data.objects.filter(LatLong_State=state).values('LatLong_County').distinct().order_by('LatLong_County')
        counties = []
        
        for row in fetched_counties:
            if str(row['LatLong_County']) != "None":
                #if str(row['COUNTY']) != "None":
                counties.append(str(row['LatLong_County']))
        
        #serializer = DistinctCountySerializer(counties, context={'request': request}, many=True)
        
        return Response(counties)

@api_view(['Get'])
def geojson_list(request):
    if request.method == 'GET':
        # queryset = Data.objects.filter(STATE='TX').values('STATE', 'LATITUDE', 'LONGITUDE')
        # serialized = json.dumps(list(queryset), cls=DjangoJSONEncoder)
        #return Response(serialize('geojson', Data.objects.filter(STATE='TX').values(), geometry_field='point', fields=('name',)))
        #return Response(serialize)
        fod_id = Data.objects.values_list('FOD_ID', flat=True)
        fire_name = Data.objects.values_list('FIRE_NAME', flat=True)
        fyear = Data.objects.values_list('DISCOVERY_DATE', flat=True)
        fcause = Data.objects.values_list('NWCG_GENERAL_CAUSE', flat=True)
        fcont = Data.objects.values_list('CONT_DATE', flat=True)
        fsize = Data.objects.values_list('FIRE_SIZE', flat=True)
        lat = Data.objects.values_list('LATITUDE', flat=True)
        long = Data.objects.values_list('LONGITUDE', flat=True)
        fstate = Data.objects.values_list('STATE', flat=True)
        fcounty = Data.objects.values_list('FIPS_NAME', flat=True)

        geo_json = [ {"type": "Feature",
                    "properties": {
                        "id":  ident,
                        "popupContent":  "id=%s" % (ident,),
                        "name":  fname,
                        "Discovery_Date": ffyear,
                        "Containment_Date": ffcont,
                        "Cause": ffcause,
                        "State": ffstate,
                        "County": ffcounty,
                        "Size": ffsize
                        },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [lon,lat] }}
                    for ident,fname,ffyear,ffcont,ffcause,ffstate,ffcounty,ffsize,lon,lat in zip(fod_id,fire_name,fyear,fcont,fcause,fstate,fcounty,fsize,long,lat) ]
        return Response(geo_json)

@api_view(['Get'])
def csv_view(request):
    if request.method == 'GET':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="fires.csv"'

        writer = csv.writer(response)
        fire_rows = Data._meta.fields

        fire_columns = [f.name for f in Data._meta.fields]

        writer.writerow(fire_columns)

        fires = Data.objects.values_list()
        for fire in fires:
            writer.writerow(fire)
        return response
    
#@api_view(['Get'])
#def distinct_field_list(request):
#    if request.method == 'GET':
#        #get categories param and turn it into list
#        categories = request.query_params.get('CATEGORIES',None)
#        categories = categories.split(',')
#
#        #add FOD_FPA as a default
#        if categories[0]=='' and len(categories)==1:
#            categories.addAllCategories()
#        #add FOD_ID no matter what
#        categories_list = categoryHelper(categories)
#        if 'FOD_ID' not in categories_list:
#            categories_list.insert(0, 'FOD_ID')
#        
#        return Response(categories_list)


def administrator(request):
    return HttpResponse("Hello you are looking at the administrator page.")


def execute_csv_import(file_path):
    # Define the required parameters and paths.
    # Make sure to update these values based on nvironment.
    csv = file_path
    createtable_sql = './sql/createtable.sql'  # Path to createtable.sql
    docker_mysql_container = 'ffp-mysql'
    mysql_user = 'root'
    mysql_password = 'mysql-root-password'
    mysql_database = 'ffp-mysql-db'

    # Run the necessary Docker commands.
    subprocess.run(['docker', 'cp', createtable_sql, f'{docker_mysql_container}:./var/lib/mysql-files/'])
    subprocess.run(['docker', 'cp', csv, f'{docker_mysql_container}:./var/lib/mysql-files/'])

    # Wait for the database connection to be open before running the import
    wait_count = 1
    while wait_count <= 10:
        try:
            subprocess.run(['docker', 'exec', '-i', docker_mysql_container, 'mysql', f'-u{mysql_user}', f'-p{mysql_password}', '-e', 'status'])
            break
        except subprocess.CalledProcessError:
            print("Waiting for database connection...")
            time.sleep(5)
            wait_count += 1

    # Run the MySQL commands to create the table and import the data
    mysql_commands = f"use {mysql_database}; source /var/lib/mysql-files/createtable.sql; LOAD DATA INFILE '/var/lib/mysql-files/{csv}' IGNORE INTO TABLE FPA_FOD_PLUS FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\\n' IGNORE 1 LINES SET CONT_DATE = date_format(str_to_date(CONT_DATE, '%m/%d/%Y %T'), '%Y-%m-%d %T');"
    subprocess.run(['docker', 'exec', '-i', docker_mysql_container, 'mysql', f'-u{mysql_user}', f'-p{mysql_password}'], input=mysql_commands, text=True)

    # Restart the MySQL and Django containers to re-initialize the connection
    subprocess.run(['docker', 'restart', docker_mysql_container])

    wait_count = 1
    while wait_count <= 10:
        try:
            subprocess.run(['docker', 'exec', '-i', docker_mysql_container, 'mysql', f'-u{mysql_user}', f'-p{mysql_password}', '-e', 'status'])
            break
        except subprocess.CalledProcessError:
            print("Waiting for database connection...")
            time.sleep(5)
            wait_count += 1

    subprocess.run(['docker', 'restart', 'ffp-django'])


def csv_upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['csv_file']
        if not uploaded_file.name.endswith('.csv'):
            messages.error(request, 'Invalid file format. Please upload a CSV file.')
            return HttpResponseRedirect(reverse('csv_upload'))

        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_path = fs.path(filename)
        try:
            # Replace the content of the csv-data-import.sh script with a Python function to perform the same operations
            execute_csv_import(file_path)

            messages.success(request, 'CSV file uploaded and processed successfully.')
        except Exception as e:
            messages.error(request, 'Error processing CSV file: ' + str(e))
        finally:
            os.remove(file_path)
            return HttpResponseRedirect(reverse('csv_upload'))

    return render(request, 'csv_upload.html')
