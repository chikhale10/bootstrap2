
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .models import ContactUs 

# Create your views here.
def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def login(request):
   
    if request.method == "POST":
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        
        user = authenticate(request, email=email, password=pass1)
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            messages.error(request, "Invalid credentials")
            return redirect('index')
    
    return render(request, 'login.html')

   


def Registration(request):
    
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('Registration')  # Redirect back to registration page
        
        # Check if email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")
            return redirect('Registration')  # Redirect back to registration page
        
        # Create and save the user object
        try:
            user = User.objects.create_user(username=name, email=email, password=password1)
            messages.success(request, "Your account has been successfully created")
            return redirect("login")
        except Exception as e:
            messages.error(request, f"Error creating user: {str(e)}")
            return redirect('Registration')  # Redirect back to registration page
    
    return render(request, 'Registration.html')





def ContactUs(request):
    
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('msg')

        # Create a new Contact object and save it to the database
        ContactUs.objects.create(full_name=full_name, email=email, mobile=mobile, message=message)

        # Redirect to a success page or return a response as needed
        return HttpResponseRedirect('ContactUs.html')  # You can replace '/success/' with the URL of your success page
    else:
        # Render the initial contact form
        return render(request , 'ContactUs.html') 
    

def AboutUs(request):
    return render(request,"AboutUs.html")
