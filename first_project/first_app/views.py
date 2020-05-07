from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from django import forms
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import auth_login, auth_logout
from first_app.models import Topic, Webpage, AccessRecord, User
from . import forms
from first_app.forms import NewUserForm, UserForm, UserProfileInfoForm
from first_app import views

# from first_app import forms
#Each view is going to be created as a separate function (see index below)
#Each view is going to take in at least one module, and must return an HttpResponse object

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dictionary = {'access_records': webpages_list}
    my_dictionary = {'insert_me' : "Hello I am from views.py",}
    return render(request,'first_app/new_index.html', context=date_dictionary)

def help(request):
    help_dictionary = {"help_insert": "Help Page"}
    return render(request, 'first_app/help.html', context=help_dictionary)

# def form_name_view(request):
#     form = forms.FormName()
#     return render(request, 'form_name.html',
#                     {'form':form})

def form_name_view(request):
    form = forms.FormName()

    #Check to see if we get a POST back.
    if request.method == "POST":
        #In which case we oass in that request.
        form = forms.FormName(request.POST)

    #Check to see form is valid
        if form.is_valid():
            # Do something
            print("VALIDATION SUCCESS!")
            print("Form Validation Success. Prints in console.")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])
    return render(request, 'first_app/form_page.html', {'form':form})


def users(request):

    user_list = User.objects.order_by("first_name")
    user_dict = {'users':user_list}
    # if request.method == "POST":
    #     form = NewUserForm(request.POST)
    #
    #     if form.is_valid():
    #         form.save(commit=True)
    #         return index(request)
    #     else:
    #         print("Error. Form invalid.")

    return render(request, "first_app/users.html", context=user_dict)

######### See login at bottom for update login page
# def login_page(request):
#
#     form = NewUserForm()
#
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#
#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print("Error. Form invalid.")
#
#     return render(request, "first_app/login.html", {"form": form})


def home(request):
    context_dict = {'text':'hello world', 'number':100}
    return render(request, 'first_app/home.html', context_dict)

def other(request):
    return render(request, 'first_app/other.html')

def relative(request):
    return render(request, 'first_app/relative_url_temp.html')

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)

            profile.user = user

            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context_dict = {"user_form": user_form, "profile_form":profile_form}

    return render(request, "first_app/registration.html", context_dict)


def user_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                print("ACTIVE")
                #### line below returns error.. investigate later
                # return HttpResponseRedirect(reverse('index'))
                return redirect("first_app:home")
            else:
                print("ACTIVE")
                return HttpResponse("Username or Password is invalid.")
        else:
            print("Someone tried to login and failed.")
            print("Failed Credentials = Username: {} and Password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    return render(request, "first_app/user_login.html", {})

@login_required
def user_logout(request):
    logout(request)
    # return HttpResponseRedirect(reverse("user_login"))
    return redirect("first_app:person_login")

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")



