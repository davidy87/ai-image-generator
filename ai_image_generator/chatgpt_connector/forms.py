from django import forms
from django.forms import ModelForm
from chatgpt_connector.models import *


class ImgForm(forms.Form):
    image = models.ImageField(null=True, blank=True, upload_to='result/')

# class Form(ModelForm):
#     class Meta:
#         model = Image
#         fields = ['description', 'size']