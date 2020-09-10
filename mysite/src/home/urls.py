from django.conf.urls import url ,include
from . import views
from django.contrib.auth.views import LoginView , LogoutView , PasswordResetCompleteView , PasswordResetView , PasswordResetConfirmView ,  PasswordResetDoneView

urlpatterns = [
    #url(r'^$', views.home),
    #url('accounts/', include('django.contrib.auth.urls')),
    url(r'^$', views.home, name='home'),
]
