from django.shortcuts import render ,redirect , HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm , PasswordChangeForm
from accounts.forms import EditProfileForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.


def home(request):
    
    return render (request, 'home.html')
