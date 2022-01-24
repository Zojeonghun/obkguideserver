
from django.shortcuts import render
from django.urls import path
from knees import views
from . import views


app_name = 'feets'

urlpatterns = [
    path('', views.FeetPage, name="feets"),
    path('search/', views.search, name='search'),
    path('<int:pk>/', views.FeetDetailView.as_view(), name='feet-detail'),
    path('feets_list_all', views.FeetListAllFilter, name='feets-list-all'),
    path('feets_admin_list/', views.FeetAdminListView.as_view(), name='feets-admin-list'),
    path('feets_admin_list/<int:pk>/', views.FeetAdminUpdateView.as_view(), name='feet-admin-update'),
    path('<int:pk>/delete/',views.FeetDeleteView.as_view(),name="feet-admin-delete",),
    path('add/', views.FeetAdminCreateView.as_view(), name='feet-admin-create'),
]