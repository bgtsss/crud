from django.urls import path
from .views import (
    HomePageView, AboutPageView,
    RoleListView, RoleDetailView, 
    RoleCreateView, RoleUpdateView, RoleDeleteView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('roles/', RoleListView.as_view(), name='role_list'),
    path('roles/<int:pk>/', RoleDetailView.as_view(), name='role_detail'),
    path('roles/create/', RoleCreateView.as_view(), name='role_create'),
    path('roles/<int:pk>/update/', RoleUpdateView.as_view(), name='role_update'),  # Use this as the default update path
    path('roles/<int:pk>/delete/', RoleDeleteView.as_view(), name='role_delete'),
]
