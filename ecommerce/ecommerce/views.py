from django.shortcuts import render

from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.shortcuts import redirect
def index(request):
    return render(request,'index.html')


def signupform(request):
    return render(request,'signup.html')

def signup(request):
     if request.method=="POST":
         #get post parameters
         username=request.POST.get('username')
         fname=request.POST['fname']
         lname=request.POST['lname']
         email=request.POST['email']
         password1=request.POST['password1']
         password2=request.POST['password2']
         
         #check for error inputs
         
         #username under 10 chars
         if len(username) < 2 or len(username) > 10 :
             messages.error(request,"Username must be under 10 characters and min 2")
             return redirect('index')
             
        #username must be alphabets and numbers
         if not username.isalpha():
             messages.error(request,"Username should only contain letters and numbers")
             return redirect('index')
          
        #passwords should match   
         if password1!=password2:
             messages.error(request,"Password do not match")
             return redirect('index')
         
         
         #create user
         myuser=User.objects.create_user(username,email,password1)
         myuser.first_name=fname
         myuser.last_name=lname
         myuser.save()
         messages.success(request,"Your iCoder account has been successfully created.")
         return redirect('/')
     else:
        return HttpResponse("404 -Not found")
    
def handlelogin(request):
    
    if request.method=="POST":
        #get post parameters
        loginusername=request.POST.get('username')
        loginpassword=request.POST.get('password')
        
        user=authenticate(username=loginusername,password=loginpassword)
        
        #if password is wrong user become None
        
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In ")
            return redirect('/shop')
        else:
            messages.error(request,"Invalid credentials, PLease try again")
            return redirect('/')
        
    else:
        return HttpResponse("404 -Not found")
    
def handlelogout(request):
        logout(request)
        messages.success(request,"Successfully logged out")
        return redirect('/')