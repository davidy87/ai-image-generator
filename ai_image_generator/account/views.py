from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.urls import reverse

from .forms import UserForm


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
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