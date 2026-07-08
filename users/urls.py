from django.urls import path

from .views import CustomLoginView, CustomLogoutView, RegisterView, UserUpdateView

app_name = "user"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("user_update/<int:pk>/", UserUpdateView.as_view(), name="user_update"),
]
