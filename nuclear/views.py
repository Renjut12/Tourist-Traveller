from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method == 'POST':
        USERNAME = request.POST['username']
        PASSWORD = request.POST['password']
        client = auth.authenticate(username=USERNAME,password=PASSWORD)

        if client is not None:
            auth.login(request,client)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        USERNAME     = request.POST['username']
        FIRST_NAME   = request.POST['first_name']
        LAST_NAME    = request.POST['last_name']
        EMAIL       = request.POST['email']
        PASSWORD     = request.POST['password']
        CON_PASSWORD = request.POST['password1']

        if PASSWORD==CON_PASSWORD:
            if User.objects.filter(username=USERNAME).exists():
                messages.info(request,"username taken")
                return redirect('register')

            elif User.objects.filter(email= EMAIL).exists():
                messages.info(request,"email is taken")
                return redirect('register')

            else:
                client = User.objects.create_user(username=USERNAME,first_name=FIRST_NAME,last_name=LAST_NAME,
                                          email=EMAIL, password=PASSWORD )

                client.save();
                return redirect('login')

        else:
            messages.info(request,"Password is incorrect")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")



