from django.urls import path
from . import views
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    QuestionView,
                    QuestionDetailView,
                    QuestionCreateView,
                    QuestionUpdateView,
                    AnswerCreateView,
                    NoAnswerQuestionuestionView,
                    UserListView,
                    NewsListView,
                    CreateNews,
                    NewsUpdateView,
                    NewsDeleteView)

urlpatterns = [
    path('', views.home, name='home'),
    path('qa/', QuestionView.as_view(), name='qa'),
    path('qa/new/', QuestionCreateView.as_view(), name='qa-new'),
    path('qa/<int:pk>/', QuestionDetailView.as_view(), name='q-detail'),
    path('qa/<int:pk>/answer/', AnswerCreateView.as_view(), name='answer'),
    path('qa/<int:pk>/update', QuestionUpdateView.as_view(), name='q-update'),
    path('noanswer/', NoAnswerQuestionuestionView.as_view(), name='noanswer'),
    path('about/', views.AboutView, name='about'),
    path('team/', UserListView.as_view(), name='team'),


    path('about/', views.about, name='about'),
    # path('posts/', views.posts, name='posts'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('login/', views.login, name='login'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/create/', CreateNews.as_view(), name='create-news'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='update-news'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='delete-news'),
]
