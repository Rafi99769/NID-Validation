from django.db import models
from conf.constants import BLOOD_GROUPS


class NID(models.Model):
    name = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=50)
    mothers_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    number = models.CharField(max_length=20)
    address = models.TextField()
    blood_group = models.PositiveSmallIntegerField(choices=BLOOD_GROUPS, default=3)
    received_date = models.DateField()

    def __str__(self):
        return self.number
