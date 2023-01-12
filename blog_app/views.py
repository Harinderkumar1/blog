from django.shortcuts import render,redirect
from .forms import blog_form
from .models import Blog
from .forms import contact_form
from .models import contact
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import profile
from .forms import profile_form
# Create your views here.

@login_required(login_url='login')
def add_blog(request):
    if request.method=='GET':
        form=blog_form()
        return render(request,'addblog.html',{'form':form})

    else:
        form=blog_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addblog')


@login_required(login_url='login')
def show(request):
    data=Blog.objects.all()
    return render(request,'home.html',{'data':data})


def delete(request,id):
    data=Blog.objects.get(id=id)
    data.delete()
    return redirect('addblog')




def update(request,id):
    data = Blog.objects.get(id=id)
    if request.method=='GET':
        form=blog_form(instance=data)
        return render(request,'addblog.html',{'form':form})

    else:
        form=blog_form(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')
        return redirect('home') 



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Invalid Username/Password")
            return redirect('login')

    return render(request,'base.html')


def logout(request):
    auth.logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('login')
        else:
            messages.info(request,"Try Matching Password")
            return redirect('signup')

    return render(request,'base.html')

@login_required(login_url='login')
def add_contact(request):
    if request.method=='GET':
        data=contact_form()
        return render(request,'addcontact.html',{'data':data})

    else:
        data=contact_form(request.POST)
        if data.is_valid():
            data.save()
            return redirect('contact    ')

@login_required(login_url='login')
def contact_show(request):
    data=contact.objects.all()
    # return redirect('contacts')
    return render(request,'contact_show.html',{'data':data})

@login_required(login_url='login')
def add_profile(request):
    if request.method=='GET':
        data=profile_form()
        return render(request,'addprofile.html',{data:'data'})

    else:
        data=contact_form(request.POST)
        if data.is_valid():
            data.save()
            return redirect('profile')

# @login_required(login_url='login')
# def profile_show(request):
#     data=profile.objects.all()