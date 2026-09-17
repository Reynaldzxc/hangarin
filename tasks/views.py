from django.shortcuts import render
from .models import Task

def dashboard(request):
    total_tasks = Task.objects.count()
    pending_tasks = Task.objects.filter(status = "Pending").count()
    completed_tasks = Task.objects.filter(status = "Completed").count()
    in_progress_tasks = Task.objects.filter(status="In Progress").count()

    context = {
        "total_tasks": total_tasks,
        "pending_tasks": pending_tasks,
        "completed_tasks": completed_tasks,
        "in_progress_tasks": in_progress_tasks,
    }

    return render(request, "tasks/dashboard.html", context)