from django.shortcuts import render,redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
      user = request.user.is_authenticated
      if user:
         return redirect('/')
      else: 
         return render(request,'user/signup.html')
      
    elif request.method == 'POST':
       username = request.POST.get('username', None)
       password = request.POST.get('password', None)
       password2 = request.POST.get('password2', None)
       nickname = request.POST.get('nickname', None)
       email = request.POST.get('email', None)
       gender = request.POST.get('gender', None)
       phone = request.POST.get('phone', None)
       birth_day = request.POST.get('birth_day', None)

       if password != password2:
          return render (request, 'user/signup.html')
       elif not password: # 비밀번호를 입력하지 않았을 경우
          return render(request, 'user/signup.html')
       
       else:
          exist_user = get_user_model().objects.filter(username=username)
    

          if exist_user:
             return render(request, 'user/signup.html')
          
          else:
             UserModel.objects.create_user(username=username, password=password, nickname=nickname, email=email, gender=gender, phone=phone, birth_day=birth_day)
             
             return redirect('/log-in')



def log_in_view(request):
    if request.method == 'POST':
       username = request.POST.get('username', None)
       password = request.POST.get('password', None)

       me = auth.authenticate(request, username=username, password=password)
       if me is not None:
          auth.login(request, me)
          return redirect('/')
       else:
          return redirect('/log-in')
    elif request.method == 'GET':
       user = request.user.is_authenticated
       if user:
          return redirect('/')
       else:
          return render(request, 'user/login.html') 
       
@login_required
def logout(request):
    auth.logout(request)
    return redirect("/")