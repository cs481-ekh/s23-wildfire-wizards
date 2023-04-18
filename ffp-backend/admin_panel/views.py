from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import CSVUploadForm
from .models import AdminUser
from .utils import replace_data_with_csv
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import os
import subprocess
import time


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


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'})

    return render(request, 'admin_panel/login.html')

@login_required
def dashboard(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            execute_csv_import(request.FILES['file'].path) # Changed form replace_data_with_csv and added .path to the end
            # Provide a success message
            return JsonResponse({'success': True})
    else:
        form = CSVUploadForm()

    return render(request, 'admin_panel/dashboard.html', {'form': form})

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
