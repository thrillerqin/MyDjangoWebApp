'''为应用程序myusers定义URL模式'''
from django.urls import path,re_path
from django.contrib.auth.views import LoginView, auth_login

from django.contrib.auth import views as auth_views

from django.conf.urls import url

from . import views


urlpatterns = [
    # 显示所有主题
    # re_path('^login/$', LoginView, {'template_name': 'myusers/login.html'}, name='login'),
    # path('login/', LoginView, {'template_name': 'myusers/login.html'}, name='login'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='myusers/login.html'), name='login'),
    url(r'^logout/$', views.my_logout_view, name = 'logout'),
    url(r'^register/$', views.my_register, name = 'my_register'),
    # path('login/', auth_views.LoginView.as_view(template_name='generales/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='generales/login.html'), name='logout'),
]