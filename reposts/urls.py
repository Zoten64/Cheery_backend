from django.urls import path
from reposts import views

urlpatterns = [
    path('', views.RepostList.as_view()),
    path('<int:pk>/', views.RepostDetail.as_view()),
]
