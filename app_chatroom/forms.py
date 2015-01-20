from django import forms
from models import *
from forms import *


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'rows':"1",'placeholder':"say something..."}),
        }