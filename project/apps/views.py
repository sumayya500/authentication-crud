from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SignupForm, LoginForm
from .models import CustomUser
from django.db.models import Q
from django.views.decorators.cache import never_cache
from django.contrib.auth import update_session_auth_hash
from .forms import UserEditForm



def login_view(request):
      form = LoginForm(request.POST or None) 
      if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    print('success')
                    return redirect('admin_dashboard') 
                return redirect('home')  
            else:
                form.add_error(None, 'Invalid login credentials')
      return render(request,'apps/login.html',{'form' : form})

def signup_view(request):
      if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
      else:
        form = SignupForm()
      return render(request,'apps/signup.html',{'form':form})



@login_required
@never_cache
def home_view(request):
    return render(request,'apps/home.html')

def is_super_admin(user):
    return user.is_super_admin

@login_required
def admin_dashboard(request):
    query = request.GET.get('q')
    if query:
        user = CustomUser.objects.filter(username__icontains=query)

        return render(request,'apps/admin_dashboard.html', {'users': user})
    else:
        users = CustomUser.objects.all()
    return render(request,'apps/admin_dashboard.html', {'users': users})

@login_required
def delete_user(request,user_id):
    user = CustomUser.objects.get(id=user_id)
    user.delete()
    return redirect('admin_dashboard')


@login_required
def edit_user(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
        form =UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = UserEditForm(instance=user)
    return render(request, 'apps/edit_user.html', {'form': form , 'user':user} )


@user_passes_test(is_super_admin)
@login_required
def create_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = SignupForm()
    return render(request,'apps/signup.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')