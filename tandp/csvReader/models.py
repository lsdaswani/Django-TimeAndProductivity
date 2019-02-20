from django.db import models

class CsvData(models.Model):
    processName = models.CharField(max_length = 100)
    processId = models.CharField(max_length = 100)
