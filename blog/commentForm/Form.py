from django import forms
from blog.models import Comment
class commentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','text','post']