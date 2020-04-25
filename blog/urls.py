from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views

urlpatterns=[
    path('',PostListView.as_view(),name='blog-home'), #path to call class based views from url
    #path('',views.home,name='blog-home'), path for blog home page on fucntion based views
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),#it:pk represents integer primary key , in url, we defined to just put number to go to blogs
    path('about/',views.about,name='blog-about'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),

]
