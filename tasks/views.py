from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

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

def task_list(request):
    tasks = Task.objects.all()

    context = {
        "tasks": tasks,

    }

    return render(request, "tasks/task_list.html", context)

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "tasks/task_form.html", context)