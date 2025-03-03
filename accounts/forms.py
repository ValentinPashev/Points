from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from accounts.models import Profile


class CustomStudentFrom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', )

    def __init__(self, *args, **kwargs):
        super(CustomStudentFrom, self).__init__(*args, **kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None


class CustomStudentChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = '__all__'

class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'faculty_number', 'branch', 'profile_picture')


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'faculty_number', 'branch', 'profile_picture')

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = Profile
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None
