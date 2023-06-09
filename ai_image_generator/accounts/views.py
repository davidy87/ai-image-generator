from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.utils.safestring import mark_safe
from .forms import UserForm


# Create your views here.
def logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect(request.path_info)
        else:
            messages.error(request, mark_safe('Username or Password is incorrect.'))

    return redirect('/')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            messages.success(request, 'You have signed up', extra_tags='signup_success')
            return redirect('/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.add_message(request, messages.ERROR, mark_safe(error))

            return redirect('/')
    
    form = UserForm()
    return render(request, 'chatgpt_connector/index.html', {'form': form})


# class UserCreateView(CreateView):
#     form_class = UserForm
#     template_name = 'account/signup.html'
#     success_url = "/"