# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    def __unicode__(self):
        return self.name
    def as_dict(self):
        return {
            "name":self.name,
            "occupation": self.occupation,
            "date_of_birth":self.date_of_birth
        }