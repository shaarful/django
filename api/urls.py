from django.urls import path, include
from . import views

app_name = 'api'
urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('users/', views.UserList.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('hello', views.ApiEndpoint.as_view()),
    path('secret', views.secret_page, name='secret'),
]
