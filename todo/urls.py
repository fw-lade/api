from django.urls import path
from todo import views

urlpatterns = [
    path('', views.createtodo, name = 'createtodo'),
    path('alltodo/', views.alltodo, name = 'alltodo'),
    path('deletetodo/<int:id>/', views.deletetodo, name = 'deletetodo'),
    path('tododetails/<int:id>/', views.tododetails, name = 'tododetails'),
    path('todoedit/<int:id>/', views.todoedit, name = 'todoedit'),
]