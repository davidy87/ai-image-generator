from django.shortcuts import render
from chatgpt_connector.forms import *


# Create your views here.
def index(request):
    form = Form()
    return render(request, 'chatgpt_connector/index.html')


def generator(request):
    return render(request, 'chatgpt_connector/generator.html')