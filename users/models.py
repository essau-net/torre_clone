from django.contrib.auth.models import AbstractUser
from django.db.models import BigAutoField, CharField, IntegerField, DateTimeField, ImageField

# Create your models here.

class User(AbstractUser):
    id = BigAutoField(primary_key=True)
    username = CharField(max_length=255, unique=True)
    password = CharField(max_length=255, null=False)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=155)
    email = CharField(unique=True, max_length=255)
    professional_role = CharField(max_length=255, blank=True, null=True)
    cellphone_number = CharField(unique=True, max_length=13, blank=True, null=True)
    image_perfil = CharField(blank=True, null=True, max_length=255)
    language = CharField(max_length=2, blank=True, null=True)
    is_staff = IntegerField(default=False)
    is_active = IntegerField(default=True)
    is_superuser = IntegerField(default=False)
    last_login = DateTimeField(blank=True, null=True)
    date_joined = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        managed: bool = False
        db_table: str = 'users'