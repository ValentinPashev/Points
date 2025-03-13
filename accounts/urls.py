from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path
from accounts.views import profile_view, EditProfileView, ChangePasswordView, activate, register, \
    search_users_view, CustomResetPasswordView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', profile_view, name='profile'),

    path('activate/<uidb64>/<token>', activate, name='activate'),

    path("profile/edit/<int:pk>/", EditProfileView.as_view(), name="profile-edit"),
    path("profile/password-change/<int:pk>/", ChangePasswordView.as_view(), name="change-password"),

    path("reset-password/", CustomResetPasswordView.as_view(), name="password_reset"),
    path("reset-password/done/",
         PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),
         name="password_reset_done"),
    path("reset-password/confirm/<uidb64>/<token>/",
         PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path("reset-password/complete/",
         PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
         name="password_reset_complete"),
    path("search/", search_users_view, name="profile_search"),

]
