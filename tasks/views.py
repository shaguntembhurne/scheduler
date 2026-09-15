import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Task

def homepage_view(request):
    if request.method == "POST":
        if 'add_task' in request.POST:
            task_title = request.POST.get("title")
            if task_title:
                Task.objects.create(title=task_title)
                
        elif 'delete_task' in request.POST:
            task_id = request.POST.get("task_id")
            Task.objects.filter(id=task_id).delete()
            
        elif 'toggle_task' in request.POST:
            task_id = request.POST.get("task_id")
            task = get_object_or_404(Task, id=task_id)
            task.is_completed = not task.is_completed
            task.save()
            
        return redirect('homepage')

    # Order tasks so uncompleted are at top, completed at bottom
    tasks = Task.objects.all().order_by('is_completed', '-created_at')
    return render(request, 'tasks/homepage.html', {'tasks': tasks})

def focus_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/focus.html', {'task': task})

def save_time_view(request, task_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            added_seconds = int(data.get("time_spent", 0))
            task = get_object_or_404(Task, id=task_id)
            task.time_spent += added_seconds
            task.save()
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error"}, status=400)
    return JsonResponse({"status": "invalid"}, status=400)