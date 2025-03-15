from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from jet.admin import CompactInline
from accounts.models import AppStudent, Profile


class ProfileInline(CompactInline):
    model = Profile
    extra = 0


@admin.register(AppStudent)
class AppStudentAdmin(UserAdmin):
    list_display = ('email', 'username', 'faculty_number', 'is_staff', 'is_active', 'can_approve_events')
    list_filter = ('is_staff', 'is_active', 'can_make_reports')
    search_fields = ('email', 'username', 'faculty_number')
    ordering = ('email',)
    fieldsets = (
        (None,
         {'fields': ('email', 'password', 'can_make_reports', 'can_approve_events')}),
        (_('Personal Info'), {'fields': ('username', 'faculty_number')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important Dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None,
         {
            'classes': ('wide',),
            'fields': ('email', 'username', 'faculty_number', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )
    inlines = [ProfileInline]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'branch', 'role', 'points_from_events')
    list_filter = ('branch', 'role')
    search_fields = ('first_name', 'last_name', 'user__email')
