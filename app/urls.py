from django.contrib.auth import views as auth_views
from django.urls import path

from .views import profile_details, upload_file, all_files

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.
         as_view(), name='password_change_done'),
    path('profile/', profile_details, name="profile"),
    path('upload/', upload_file, name="upload"),
    path('all_files/', all_files, name="all_files")
]
