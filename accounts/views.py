from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.forms import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from accounts.forms import CustomStudentFrom, ProfileCreationForm, ProfileChangeForm, ChangePasswordForm
from accounts.models import Profile


# Create your views here.

class RegisterView(CreateView):
    form_class = CustomStudentFrom
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')


def create_profile_or_display_view(request):
    profile = request.user.profile

    is_profile_complete = all([
        profile.first_name,
        profile.last_name,
        profile.branch,
    ])

    if is_profile_complete:

        context = {
            'profile': profile,

        }
        return render(request, 'accounts/profile_details.html', context)

    else:
        print(request.FILES)
        if request.method == 'POST':
            form = ProfileCreationForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse_lazy('profile'))
        else:
            form = ProfileCreationForm(instance=profile)
            print(form.errors)

        context = {
            'form': form,
        }
        return render(request, 'accounts/complete_profile_page.html', context)


class EditProfileView(UpdateView):
    model = Profile
    template_name = 'accounts/update-profile.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'pk'

    def get_form_class(self):
        return modelform_factory(Profile, fields=('first_name', 'last_name', 'faculty_number', 'branch', 'profile_picture'))


class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('index')
    template_name = 'accounts/change_password.html'

