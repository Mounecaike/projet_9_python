from django.urls import path
from follows import views

app_name = 'follows'

urlpatterns = [
    path('', views.list_follows, name="list_follows"),
    path('delete/<int:pk>/', views.delete_follow, name="delete_follow"),
    path('block/<int:pk>/', views.block_user, name="block_user"),
    path('unblock/<int:pk>/', views.unblock_user, name="unblock_user"),
]
