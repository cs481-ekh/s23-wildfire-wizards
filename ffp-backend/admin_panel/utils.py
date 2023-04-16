
import csv
from io import TextIOWrapper
from FPA_FOD_PLUS.models import Data

def replace_data_with_csv(csv_file):
    csv_data = TextIOWrapper(csv_file.file, encoding='utf-8')
    reader = csv.reader(csv_data)
    
    next(reader, None)  # Skip header

    # Clear existing data
    Data.objects.all().delete()

    # Replace with new data
    for row in reader:
        your_model_instance = Data(
            FOD_ID=row[0], 
            FPA_ID=row[1],
            SOURCE_SYSTEM_TYPE=row[2],
            SOURCE_SYSTEM=row[3],
            NWCG_REPORTING_AGENCY=row[4],
            NWCG_REPORTING_UNIT_ID=row[5],
            NWCG_REPORTING_UNIT_NAME=row[6],
            SOURCE_REPORTING_UNIT=row[7],
            SOURCE_REPORTING_UNIT_NAME=row[8],
            LOCAL_FIRE_REPORT_ID=row[9],
            LOCAL_INCIDENT_ID=row[10],
            FIRE_CODE=row[11],
            FIRE_NAME=row[12],
            ICS_209_PLUS_INCIDENT_JOIN_ID=row[13],
            ICS_209_PLUS_COMPLEX_JOIN_ID=row[14],
            MTBS_ID=row[15],
            MTBS=row[16],
            )
        your_model_instance.save()