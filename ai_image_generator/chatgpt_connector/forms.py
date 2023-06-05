from django.forms import ModelForm
from chatgpt_connector.models import *


class Form(ModelForm):
    class Meta:
        model = Image
        fields = ['description', 'size']