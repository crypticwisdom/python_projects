from django.urls import path
from .views import index, delete, update

app_name = 'todo'

urlpatterns = [
    path('', index, name="index"),
    path('delete/<int:q_id>', delete, name="delete"),
    path('update/<int:q_id>', update, name="update")
]