from django.conf.urls import url ,include
from . import views


urlpatterns = [
    #url(r'^$', views.home),
    #url('accounts/', include('django.contrib.auth.urls')),
    url(r'^$', views.home, name='home'),
]
