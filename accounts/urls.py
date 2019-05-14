from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('', views.login_page, name = 'login'),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'accounts/logout.html'), name = 'logout'),
    path('profile/', views.user_profile, name = 'profile')
]
