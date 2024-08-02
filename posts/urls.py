from django.urls import path
from posts import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('attachments/', views.AttachmentList.as_view()),
    path('attachments/<int:pk>/', views.AttachmentDetail.as_view()),
    path('tags/', views.TagList.as_view()),
]
