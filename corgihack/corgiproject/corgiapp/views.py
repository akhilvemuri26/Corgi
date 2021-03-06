from django.shortcuts import render
from corgiapp.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'corgiapp/home.html')
def secondpage(request):
    return redirect("https://pupcare.discussion.community/")
    # return render(request, 'corgiapp/secondpage.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'corgiapp/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:

            login(request, user)
            return HttpResponseRedirect(reverse('portal'))

        else:
            print("ERROR: USERNAME: {} and password {}".format(username, password))
            return HttpResponse("Invalid Username or Password")
    else:
        return render(request, 'corgiapp/login.html', {})

@login_required
def portal(request):

    username = request.POST.get('username')

    dog_breed = request.POST.get('dog_breed')
    profile_pictures = request.POST.get('profile_pictures')
    return render(request, 'corgiapp/portal.html', {'username': username,'profile_pictures': profile_pictures, 'dog_breed': dog_breed})
