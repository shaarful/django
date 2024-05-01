from django.urls import path

from . import views

app_name = "snippets"
urlpatterns = [
    # path('', views.snippet_list),
    # path('<int:pk>/', views.snippet_detail),
    path('', views.SnippetList.as_view(), name='list'),
    path('<int:pk>/', views.SnippetDetail.as_view()),
]
