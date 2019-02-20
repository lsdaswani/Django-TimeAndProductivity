from django.shortcuts import render
import csv
from csvReader.models import CsvData
from django.http import HttpResponse

# Create your views here.

def process_data(request):
	with open(('./csvDjango.csv')) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                _, created = CsvData.objects.get_or_create(
                    processName = row[0],
                    processId = row[1],
                    )
	return render(request,'employeeData/data.html')
