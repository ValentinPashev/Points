from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.core.exceptions import PermissionDenied
from django.forms import modelform_factory
from accounts.decorators import user_not_authenticated
from accounts.forms import CustomStudentFrom, ChangePasswordForm
from accounts.models import Profile
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.views.generic import UpdateView, ListView
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from accounts.tokens import account_activation_token
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from events.models import Event
from .forms import ProfileCreationForm


User = get_user_model()

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")
        return redirect('index')

def activate_email(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("common/activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user.username}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

@user_not_authenticated
def register(request):
    if request.method == "POST":
        form = CustomStudentFrom(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            activate_email(request, user, form.cleaned_data.get('email'))
            return redirect('index')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = CustomStudentFrom()

    return render(
        request=request,
        template_name="registration/register.html",
        context={"form": form}
        )

def profile_view(request, pk):
    user = get_object_or_404(User, id=pk)
    profile = user.profile

    is_profile_complete = all([
        profile.first_name,
        profile.last_name,
        profile.branch,
    ])

    if is_profile_complete:
        favourite_events = Event.objects.filter(favourite_by__user=user)

        context = {
            'profile': profile,
            'favourite_events': favourite_events
        }
        return render(request, 'accounts/profile_details.html', context)

    if request.method == 'POST':
        form = ProfileCreationForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('profile', args=[pk]))
    else:
        form = ProfileCreationForm(instance=profile)

    context = {'form': form}
    return render(request, 'accounts/complete_profile_page.html', context)

class EditProfileView(UpdateView):
    model = Profile
    template_name = 'accounts/update-profile.html'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})

    def get_form_class(self):
        return modelform_factory(Profile, fields=('first_name', 'last_name', 'branch', 'profile_picture'))

    def get_object(self, queryset=None):
        """ Позволява редактиране само на собствения профил """
        obj = get_object_or_404(Profile, pk=self.kwargs['pk'])
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj

class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('index')
    template_name = 'accounts/change_password.html'



def search_users_view(request):
    query = request.GET.get('q', '')

    if query:
        users = User.objects.filter(
            Q(username__icontains=query) | Q(email__icontains=query)
        )
    else:
        users = User.objects.none()

    context = {'users': users, 'query': query}
    return render(request, 'accounts/profile_search.html', context)


