from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import BooleanField

from .models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs.update({"class": "form-check-input"})
            else:
                field.widget.attrs.update({"class": "form-control"})


class CustomUserCreationForm(StyleFormMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "password1", "password2")


class CustomAuthenticationForm(StyleFormMixin, AuthenticationForm):
    pass
