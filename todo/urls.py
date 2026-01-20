from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.task_list, name="list"),
    path("<int:task_id>/toggle/", views.task_toggle, name="toggle"),
    path("<int:task_id>/delete/", views.task_delete, name="delete"),
]
