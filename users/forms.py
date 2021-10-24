#Utilities
from iso639 import languages as iso
from typing import Dict, Any
#Django 

from django.db.models.fields import IntegerField
from django.forms import CharField, fields, Form, ImageField, ValidationError 
from django.contrib.auth.forms import UsernameField
from django.forms.widgets import EmailInput

#local
from users.managers import UserManager
from users.models import User

class SignupForm(Form):
    """Sign up Form"""

    username: fields.CharField = CharField(
        min_length=6,
        max_length=255,
    )

    first_name: fields.CharField = CharField(
        min_length=2,
        max_length=255,
    )


    last_name: fields.CharField = CharField(
        min_length=2,
        max_length=155,
    )

    email: fields.CharField = CharField(
        min_length=6,
        widget=EmailInput()
    )

    password: fields.CharField = CharField(
        min_length=8,
    )

    password_confirmation: fields.CharField = CharField(
        min_length=8,
    )

    
    def clean_username(self):
        """Username must be uniqe"""

        username = self.cleaned_data['username']
        username_is_taken = User.objects.filter(username=username)

        if username_is_taken:
            raise ValidationError('Username is already in use')

        return username

    def clean_email(self):
        """Email must be unique"""

        email = self.cleaned_data['email']
        email_is_taken = User.objects.filter(email=email)

        if email_is_taken:
            raise ValidationError('Email is already in use')

        return email

    def clean(self):
        """Verify if passwords match"""

        data = super().clean()
        

        if 'password' in data and 'password_confirmation' in data:
            password = data['password']
            password_confirmation = data['password_confirmation']

            if password != password_confirmation:
                raise ValidationError('Passwords do not match')

        else:
            raise ValidationError('Passwords are required')

        return data

    def save(self):
        """Create user"""

        data = self.cleaned_data
        data.pop('password_confirmation')

        User.objects.create_user(**data)

class UpdateForm(Form):
    """Update form"""
    username: fields.CharField = CharField(
        min_length=2,
        max_length=255,
        required=True,
    )

    first_name: fields.CharField = CharField(
        min_length=2,
        max_length=255,
        required=True,
    )


    last_name: fields.CharField = CharField(
        min_length=2,
        max_length=155,
        required=True,
    )

    email: fields.CharField = CharField(
        min_length=6,
        widget=EmailInput(),
        required=True,
    )

    image_perfil: fields.ImageField = ImageField(required=False)

    professional_role: fields.CharField = CharField(
        max_length=255,
        required=False,
    )

    cellphone_number: fields.CharField = CharField(
        min_length=4,
        max_length=13,
        required=False,
    )

    language: fields.CharField = CharField(required=False)

    def clean_cellphone_number(self):
        cellphone_number = self.cleaned_data['cellphone_number']

        if cellphone_number is not None and cellphone_number != 'None' and len(cellphone_number) >= 8:
            return cellphone_number

    def clean_language(self) -> str:
        """Convert language to iso"""
        language = self.cleaned_data['language']
        
        if language is not None and language != 'None':
            language = language.title()
            
            try:
                language = iso.get(name=language).alpha2
                return language
            except KeyError:
                raise ValidationError("Please the language must be in english")
    
    def clean_professional_role(self):
        profesional_role = self.cleaned_data['professional_role']\
        
        if profesional_role is not None and profesional_role != 'None':
            return profesional_role

    def clean(self):
        data = super().clean()

        image_perfil: Any = data["image_perfil"]
        username: str = data["username"]
        if image_perfil is not None and username != 'None':
            user_manager = UserManager()
            data["image_perfil"] = user_manager.save_image(image=image_perfil, username=username)
        
        return data

    def save(self) -> None:
        data = self.cleaned_data
        user_manager = UserManager(fields=data)
        user_manager.create_update_query("username", data['username'], 'users')
        user_manager.update_field()

