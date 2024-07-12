from django.urls import path
from profiles import views

urlpatterns = [
    path('', views.ProfileList.as_view()),
    path('<int:pk>/', views.ProfileDetail.as_view()),
    path('<int:pk>/posts', views.ProfilePostsList.as_view()),
    path('<int:pk>/followers', views.ProfileFollowersList.as_view()),
    path('<int:pk>/owner', views.ProfileOwner.as_view()),
]