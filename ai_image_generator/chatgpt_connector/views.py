import os
import openai
from django.shortcuts import render, get_object_or_404
from django.views import generic
from chatgpt_connector.forms import *


OPENAI_API_KEY = "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"

# Create your views here.
def index(request):
    return render(request, 'chatgpt_connector/index.html')


def generator(request):
    return render(request, 'chatgpt_connector/generator.html')


def loading(request):
    return render(request, 'chatgpt_connector/loading.html')


def result(request):
    if request.method == 'POST':
        prompt = request.POST['imagePrompt']
        size = request.POST['imageSize']

        openai.api_key = OPENAI_API_KEY
        img_url = openai.Image.create(prompt=prompt, size=size)["data"][0]["url"]

    return render(request, 'chatgpt_connector/result.html', {"prompt": prompt, "img": img_url})


# class ResultView(generic.DetailView):
#     model = Image
#     template_name = 'chatgpt_connector/result.html'