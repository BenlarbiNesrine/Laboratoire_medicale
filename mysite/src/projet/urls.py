"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include , path
from projet import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.login_redirect , name='login_redirect'),
    url(r'admin/', admin.site.urls),
    url(r'home/', include('home.urls')),
    url(r'accounts/', include('accounts.urls')),
    url(r'dossierpatient/', include('dossierpatient.urls')),
    url(r'analyses/', include('analyses.urls')),
]
