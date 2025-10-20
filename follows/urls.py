from django.urls import path
from follows import views

app_name = 'follows'

urlpatterns = [
    path('', views.list_follows, name="list_follows"),
    path('delete/<int:pk>/', views.delete_follow, name="delete_follow"),
]
