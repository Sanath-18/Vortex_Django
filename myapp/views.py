from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
def index(request):
    context = {
        'name': 'Sanath',
        'age': 19,
        'nationality': 'Indian'
    }
    return render(request, 'index.html', context)


def register(request):
    if request.method == 'POST':
        username= request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatpassword = request.POST['repeatpassword']

        if password == repeatpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Usernmae Already used')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password,
                                                )

                user.save();
                return redirect('index')
        else:
            messages.info(request,'Password not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')