from django.urls import path

from posts import views

app_name = 'posts'

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('create/', views.create_ticket, name='create_ticket'),
    path('update/<int:pk>/', views.update_ticket, name='update_ticket'),
    path('delete/<int:pk>/',views.delete_ticket, name='delete_ticket'),
    path('review/create/<int:ticket_id>/', views.create_review, name='create_review'),
    path('review/<int:ticket_id>/', views.create_review_from_ticket, name='create_review_from_ticket'),

]
