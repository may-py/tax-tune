from django.contrib import admin
from django.urls import path, include
from. import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, CommentView, PostLikeView

urlpatterns = [
#    path('',views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/comment', CommentView.as_view(), name='comment'),
    path('post/<int:pk>/like', PostLikeView, name='post-like'),
    path('about/',views.about, name='blog-about')
]