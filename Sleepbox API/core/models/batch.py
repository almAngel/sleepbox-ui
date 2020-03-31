from django.db import models

""" class Batch(models.Model):
    id = models.CharField(max_length=30, primary_key=True) """

class Batch():
    device_id = ""
    timestamp = 0

    def __init__(self, **entries):
        self.__dict__.update(entries)