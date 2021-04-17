from django.db import models
from django.db.models.fields import TextField
from accounts.models import User

# Create your models here.
class Todo(models.Model):
    
    task = TextField(max_length=1000)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,db_column='user_id')

    class Meta:
        db_table = "todo"
        permissions = [
            ("single_view", "Can view single item"),
        ]