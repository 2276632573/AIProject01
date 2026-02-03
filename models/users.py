



 

 

from django.db import models
from models.baseEntity import BaseEntity

class User(BaseEntity):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150, null=True)
    type = models.CharField(max_length=30, null=True)

    
    class Meta:
        db_table = 'py_user'