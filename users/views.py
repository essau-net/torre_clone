"""Users views"""
#Utilities
from pdb import set_trace
from typing import Any, Dict

#Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.db.models.base import Model, ModelBase
from django.forms.forms import DeclarativeFieldsMetaclass
from django.http import HttpResponse
from django.urls.base import reverse_lazy
from django.utils.functional import SimpleLazyObject
from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

#local
from users.forms import SignupForm, UpdateForm
from users.models import User

# Create your views here.
class AccountInformation(LoginRequiredMixin, DetailView):
    """Account information view"""
    template_name: str = 'users/account.html'
    model: ModelBase = User

    def get_object(self) -> Any:
        """Get user information  to account.html template"""

        return self.request.user

class LoginView(auth_views.LoginView):
    """Login View"""

    template_name: str= 'users/login.html'
    redirect_authenticated_user: bool = True

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view"""
    template_name: str = 'users/login.html'

class SignUp(FormView):
    template_name: str = 'users/signup.html'
    form_class: DeclarativeFieldsMetaclass = SignupForm
    success_url: Any = reverse_lazy('users:login')

    def form_valid(self, form: DeclarativeFieldsMetaclass) -> HttpResponse:
        """Save user data"""

        form.save()
        return super().form_valid(form)

class UpdateAccountView(LoginRequiredMixin, FormView):
    template_name: str = 'users/update.html'
    model: ModelBase = User
    form_class: DeclarativeFieldsMetaclass = UpdateForm
    success_url = reverse_lazy('users:information')

    def get_object(self) -> Any:
        """Return user profile"""
        return self.request.user

    def form_invalid(self, form) ->Any:
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))
    
    def form_valid(self, form: DeclarativeFieldsMetaclass) -> Any:
        
        form.save()
        return super().form_valid(form)
