from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from gfg import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
# Create your views here.
def home(request):
    return render(request,'authentication/index.html')
    
def signup(request):
    if request.method == 'POST':
         username=request.POST['username']
         fname= request.POST['username']
         email=request.POST['email']
         password=request.POST['password']
         confirmPassword=request.POST['confirm_password']
         
         if User.objects.filter(username=username):
             messages.error(request,'username already exists')
             return redirect('home')
         if User.objects.filter(email=email):
             messages.error(request,'email already exists')
             return redirect('home')
         if len(username) > 30:
             messages.error( request,'username must be less than 30 characters')
             return redirect('home')
         if password != confirmPassword:
             messages.error(request,'password do not match!!!')
             return redirect(request,'home')
         
         myuser =User.objects.create_user( username=fname,email=email,password=password)
         myuser.is_active = False
         myuser.save()
         
         messages.success(request, "your account has been successfully been created")
         
         
         #email messages
         subject = 'welcome to telemedicine platform'
         message1 = '''
                    welcome  to telemedicine, where treatement is brought to your home 
                    we look forword to serve you with deligence 
                    working with enthisiasm making sure we save life especilaly for those who can not access hosiptal
                    well,look no further ,here we bring health services at your door step
                    
                    we have sent confirmation link to your account ,please visit your site to confirm
                    
                    Thank you for choosing our telemedicine services
                   '''
         from_email = settings.EMAIL_HOST_USER
         to_list = [myuser.email]
         send_mail(subject,message1,from_email,to_list,fail_silently = True)
         
         
         current_site = get_current_site(request)
         emailSubject =  "conffirm email to login at telemedicine"
         message2 =render_to_string('email_confirmation.html'),{
           'name':username,
           'domain': current_site_domain,
            'vid':urlsafe_b64_encode,             
         }
         
         return redirect('signin')
    return render(request,'authentication/signup.html')

def signin(request):
    if request.method == 'POST':
        Username = request.POST['username']  
        password = request.POST['password']
        
        user=authenticate(username=Username, password=password)
        
        if User is not None:
            login(request, user) 
            return render(request,'authentication/index.html')
        
        else:
            messages.error(request,'invalid user_name or password')
            return redirect('signup') 
        
    return render(request,'authentication/signin.html')

def email_confirmation(request):
    return render(request,'authentication/email_confirmation.html')


def signout(request):
    logout(request)
    return redirect('home')

def portal(request):
    return render(request,'authentication/portal.html')