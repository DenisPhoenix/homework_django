from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CustomAuthenticationForm, CustomUserCreationForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "users/registration/register.html"

    def get_success_url(self):
        return reverse_lazy("catalog:product_list")


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "users/registration/login.html"

    def get_success_url(self):
        return reverse_lazy("catalog:product_list")


class CustomLogoutView(LogoutView):
    template_name = "users/registration/logout.html"
