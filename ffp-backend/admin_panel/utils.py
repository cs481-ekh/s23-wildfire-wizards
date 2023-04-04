import csv
from io import TextIOWrapper
from yourapp.models import YourModel

def replace_data_with_csv(csv_file):
    csv_data = TextIOWrapper(csv_file.file, encoding='utf-8')
    reader = csv.reader(csv_data)
    
    next(reader, None)  # Skip header

    # Clear existing data
    YourModel.objects.all().delete()

    # Replace with new data
    for row in reader:
        your_model_instance = YourModel(field1=row[0], field2=row[1])
        your_model_instance.save()