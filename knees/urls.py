from django.urls import path
from knees import views
from . import views


app_name = 'knees'

urlpatterns = [
    path('', views.Knees, name="knees"),
    path('search/', views.search, name='search'),
    path('<int:pk>/', views.KneeDetailView.as_view(), name='knee-detail'),
    path('knees_list_all', views.KneeListAllFilter, name='knees-list-all'),
    path('knees_admin_list/', views.KneeAdminListView.as_view(), name='knees-admin-list'),
    path('knees_admin_list/<int:pk>/', views.KneeAdminUpdateView.as_view(), name='knee-admin-update'),
    path('add/', views.KneeAdminCreateView.as_view(), name='knee-admin-create'),
    path('<int:pk>/delete/',views.KneeDeleteView.as_view(),name="knee-admin-delete",),
]