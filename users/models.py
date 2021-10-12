from django.contrib.auth.models import AbstractUser
from django.db.models import BigAutoField, CharField, IntegerField, DateTimeField

# Create your models here.

class User(AbstractUser):
    id = BigAutoField(primary_key=True)
    username = CharField(max_length=255, unique=True)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=155)
    email = CharField(unique=True, max_length=255)
    professional_role = CharField(max_length=255, blank=True, null=True)
    cellphone_number = CharField(unique=True, max_length=13, blank=True, null=True)
    language = CharField(max_length=2, blank=True, null=True)
    is_staff = IntegerField()
    is_active = IntegerField()
    is_superuser = IntegerField()
    last_login = DateTimeField(blank=True, null=True)
    date_joined = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        managed: bool = False
        db_table: str = 'users'