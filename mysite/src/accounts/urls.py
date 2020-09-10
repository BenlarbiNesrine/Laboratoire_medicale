from django.conf.urls import url ,include
from . import views
from django.contrib.auth.views import LoginView , LogoutView , PasswordResetCompleteView , PasswordResetView , PasswordResetConfirmView ,  PasswordResetDoneView

urlpatterns = [
    #url(r'^$', views.home),
    #url('accounts/', include('django.contrib.auth.urls')),
    #url(r'^accueil/$', views.home, name='home'),
    url(r'^login/$' , LoginView.as_view() , {'template-name':'registration/login.html'}),
    url(r'^logout/$' , LogoutView.as_view() , {'template-name':'registration/logout.html'}),
    url(r'^profile/$' , views.view_profile , name='view_profile'),
    url(r'^profile/edit/$' , views.edit_profile , name='edit_profile'),
    url(r'^change-password/$' , views.change_password , name='change_password'),
    url(r'^reset-password/$' , PasswordResetView.as_view() , name='reset_password'),
    url(r'^reset-password/done/$' ,  PasswordResetDoneView.as_view() , name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$' ,  PasswordResetConfirmView.as_view() , name='password_reset_confirm'),
    url(r'^reset-password/complete/$' , PasswordResetCompleteView.as_view() , name='password_reset_complete'),
]
