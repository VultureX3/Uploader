from django.contrib.auth import views as auth_views
from django.urls import path

from .views import profile_details, upload_file, my_files

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile_details, name="profile"),
    path('upload/', upload_file, name="upload"),
    path('my_files/', my_files, name="my_files")
]
