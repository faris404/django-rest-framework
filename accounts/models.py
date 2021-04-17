from django.db import models
from django.db.models.fields import AutoField
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = AutoField(primary_key=True,db_column='id')
   
    class Meta:
        db_table = "users"