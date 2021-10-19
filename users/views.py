"""Users views"""
#Utilities
from pdb import set_trace
from typing import Any, Dict

#Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.db.models.base import ModelBase
from django.forms.forms import DeclarativeFieldsMetaclass
from django.urls.base import reverse_lazy
from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

#local
from users.forms import SignupForm
from users.models import User

# Create your views here.
class LoginView(auth_views.LoginView):
    """Login View"""

    template_name: str= 'users/login.html'
    redirect_authenticated_user: bool = True

class SignUp(FormView):
    template_name: str = 'users/signup.html'
    form_class: DeclarativeFieldsMetaclass = SignupForm
    success_url: Any = reverse_lazy('users:login')

    def form_valid(self, form: DeclarativeFieldsMetaclass):
        """Save form data"""

        form.save()
        return super().form_valid(form)

class AccountInformation(LoginRequiredMixin, DetailView):
    template_name: str = 'users/account.html'
    model: ModelBase = User

    def get_object(self) -> Any:
        a = self.request.user
        import pdb; set_trace
        return self.request.user