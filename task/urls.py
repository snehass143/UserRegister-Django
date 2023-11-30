from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.Logout, name='logout'),
    path('login/', views.Login, name='login'),
    path('register/', views.registration_view, name='register'),  # Removed the leading slash
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('edit/<int:user_id>/', views.edit_user, name='edit_user'),

    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
]