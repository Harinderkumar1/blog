from django import forms
from .models import Blog
from .models import contact

class blog_form(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'
        


class contact_form(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'

class profile_form(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'
        