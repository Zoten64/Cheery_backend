from django.urls import path
from reports import views

urlpatterns = [
    path('posts/', views.PostReportList.as_view()),
    path('posts/<int:pk>/', views.PostReportDetail.as_view()),
    path('users/', views.UserReportList.as_view()),
    path('users/<int:pk>', views.UserReportDetail.as_view()),
]