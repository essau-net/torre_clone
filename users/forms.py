#Django 

from django.db.models.fields import IntegerField
from django.forms import CharField, fields, Form, ValidationError 
from django.contrib.auth.forms import UsernameField
from django.forms.widgets import EmailInput

#local
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




