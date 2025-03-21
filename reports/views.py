from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.models import AppStudent
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import EventReportForm
from .models import EventReport


def update_event_report(request, event_id):
    report = get_object_or_404(EventReport, event__id=event_id)  # Взимаме отчета по event_id

    if request.method == "POST":
        form = EventReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            messages.success(request, "Отчетът е успешно обновен!")
            return redirect('dashboard')  # Замени с реалния URL
    else:
        form = EventReportForm(instance=report)  # Попълваме формата със съществуващите данни

    return render(request, 'reports/update_event_report.html', {'form': form, 'report': report})

# @user_passes_test(lambda u: u.is_staff)  # Само администратори
def approve_event_report(request, report_id):
    report = get_object_or_404(EventReport, id=report_id)

    if not hasattr(request.user, 'profile'):
        messages.error(request, "Вашият потребител няма свързан профил!")
        return redirect('some_view_name')

    if not report.completed:
        try:
            report.distribute_points(request.user.profile)  # Подаваме Profile вместо User
            messages.success(request, "Отчетът е одобрен и точките са раздадени.")
        except ValueError as e:
            messages.error(request, str(e))
    return redirect('some_view_name')
def user_autocomplete(request):
    query = request.GET.get('term', '')
    users = AppStudent.objects.filter(email__icontains=query)[:10]
    results = [{'id': user.id, 'text': user.email, 'name': user.profile.__str__()} for user in users]
    return JsonResponse(results, safe=False)
