from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accounts.views import profile_view, EditProfileView, ChangePasswordView, activate, register, \
    search_users_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', profile_view, name='profile'),

    path('activate/<uidb64>/<token>', activate, name='activate'),

    path("profile/edit/<int:pk>/", EditProfileView.as_view(), name="profile-edit"),
    path("profile/password-change/<int:pk>/", ChangePasswordView.as_view(), name="change-password"),
    path("search/", search_users_view, name="profile_search"),

]
