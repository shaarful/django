from django.urls import path, include

from . import views

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
