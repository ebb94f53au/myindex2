from django import forms
from contact.models import Message
from captcha.fields import CaptchaField,CaptchaTextInput
from django.forms import widgets
class messageForm(forms.ModelForm):
    captcha=CaptchaField(widget=CaptchaTextInput(attrs={'class':"form-captcha",
                                                        'placeholder':'验证码'}))
    class Meta:
        model=Message
        fields=['name','email','phone','message']