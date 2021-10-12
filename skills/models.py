#Utilities
from typing import Any
#Django
from django.db.models import BigAutoField, CharField, Model

# Create your models here.

class Skills(Model):
    id: Any = BigAutoField(primary_key=True)
    skill_name: Any = CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'skills'