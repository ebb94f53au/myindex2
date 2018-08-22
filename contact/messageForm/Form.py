from django import forms
from contact.models import Message
class messageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=['name','email','phone','message']