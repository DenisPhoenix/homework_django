from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView

from config.settings import EMAIL_HOST_USER

from .forms import CustomAuthenticationForm, CustomUserCreationForm
from .models import User


class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = "users/registration/register.html"

    def get_success_url(self):
        return reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # self.send_welcome_email(user.email)
        return super().form_valid(form)

    @staticmethod
    def send_welcome_email(user_email):
        subject = "Добро пожаловать в наш сервис"
        message = "Спасибо, что зарегистрировались в нашем сервисе!"
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "users/registration/users_form.html"

    def get_success_url(self):
        return reverse_lazy("catalog:product_list")


class UserUpdateView(UpdateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "users/registration/users_form.html"
    success_url = reverse_lazy("catalog:product_list")


class CustomLogoutView(LogoutView):
    template_name = "users/registration/logout.html"
