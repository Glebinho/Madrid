from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("aboutUs", views.aboutUs, name = 'aboutUs'),
    path("contact", views.contact, name = 'contact'),
    path("signup", views.handle_signup, name = 'handlesignup'),
    path("login", views.handle_login, name = 'handlelogin'),
    path("logout", views.handle_logout, name='handlelogout'),
    path("news", views.news, name= 'news')
]
