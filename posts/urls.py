from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.search, name='posts-list'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post-admin-update'),
    path('create/', views.PostCreateView.as_view(), name='post-admin-create'),
    path('<int:pk>/delete/',views.PostDeleteView.as_view(),name="post-admin-delete",),
    path('posts_admin-list/', views.PostAdminListView.as_view(), name='posts-admin-list')
]