from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleDeleteView,ArticleUpdateView,ArticleCreateVeiw,Search

urlpatterns = [
     path('', ArticleListView.as_view(),name='article_list'),
     path('<int:pk>/', ArticleDetailView.as_view() ,name='article_detail'),
     path('<int:pk>/delete/', ArticleDeleteView.as_view() ,name='article_delete'),
     path('<int:pk>/edit/', ArticleUpdateView.as_view() ,name='article_edit'),
     path('new/', ArticleCreateVeiw.as_view() ,name='article_new'),
     path('search/', Search.as_view(), name='search'),

]