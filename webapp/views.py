from . import models
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            auth.login(request, user)

            userinfo = models.User(
                Username = user.username,
                Password = user.password,
                Email=user.email
            )
            userinfo.save()
            


            return redirect('/')
        return render(request, 'webapp/signup.html')
    return render(request, 'webapp/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('uploadFile') 
        else:
            return render(request, 'webapp/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'webapp/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def home(request):
    return render(request, 'webapp/home.html')

def uploadFile(request):
    

    if request.method == "POST":
        
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]
        

        # Saving the information in the database
        document = models.Document(
            title = fileTitle,
            uploadedFile = uploadedFile,
            writter = User.objects.first()
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "webapp/upload-file.html", context = {
        "files": documents
    })


def play_music(request):
    music = models.Document.objects.all()
    return render(request, 'Upload-file.html',{"music":music})