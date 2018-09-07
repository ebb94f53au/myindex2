from django import forms
from blog.models import Comment
from captcha.fields import CaptchaField,CaptchaTextInput
class commentForm(forms.ModelForm):
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'class': "form-captcha",
                                                          'placeholder': '验证码'}))
    class Meta:
        model=Comment
        fields=['name','email','text','post']