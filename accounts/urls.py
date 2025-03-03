from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accounts.views import RegisterView, create_profile_or_display_view, EditProfileView, ChangePasswordView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('profile/', create_profile_or_display_view, name='profile'),

    path("profile/edit/<int:pk>/", EditProfileView.as_view(), name="profile-edit"),
    path("profile/password-change/<int:pk>/", ChangePasswordView.as_view(), name="change-password"),

]
