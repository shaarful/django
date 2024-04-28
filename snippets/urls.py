from django.urls import path

from . import views

urlpatterns = [
    # path('', views.snippet_list),
    # path('<int:pk>/', views.snippet_detail),
    path('', views.SnippetList.as_view()),
    path('<int:pk>/', views.SnippetDetail.as_view()),
]
