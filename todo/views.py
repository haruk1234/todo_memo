from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    # 追加処理（フォームからPOSTされたら追加）
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            Task.objects.create(title=title)
        return redirect("todo:list")

    tasks = Task.objects.order_by("is_done", "-created_at")
    return render(request, "todo/task_list.html", {"tasks": tasks})

def task_toggle(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_done = not task.is_done
    task.save()
    return redirect("todo:list")

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("todo:list")
