from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pages/logout.html'), name='logout'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('browseall/', views.browseall, name='browseall'),
    path('ONsearch', views.ONsearch, name="ONsearch")
    # path('updateform/', views.updateform, name='updateform')
]