from django.shortcuts import render ,redirect , HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm , PasswordChangeForm
from accounts.forms import EditProfileForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.





def view_profile(request):
   args ={'user': request.user}
   return render(request , 'registration/profile.html' , args)




def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST , instance = request.user)

        if form.is_valid() :
            form.save()
            return redirect('/accounts/profile')

    else:
        form = EditProfileForm(instance = request.user)
        args = {'form':form}
        return render (request , 'registration/edit_profile.html' , args)




def change_password(request):
  if request.method == 'POST':
      form = PasswordChangeForm(data=request.POST , user = request.user)

      if form.is_valid() :
          form.save()
          update_session_auth_hash(request , form.user)
          return redirect('/accounts/profile')
      else :
          return redirect('accounts/change_password')

  else:
      form = PasswordChangeForm(user = request.user)

      args = {'form':form}
      return render (request , 'registration/change_password.html' , args)
