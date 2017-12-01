
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.forms import ModelForm
#import re

attrs_dict = {'class': 'required'}



class RegistrationForm(forms.ModelForm):

    """
    Form for registering a new user account.
    
    
    requires the password to be entered twice to catch typos.
    
   """

    class Meta:
        model = User
        fields = ('email','first_name','last_name','password1','password2')

    
    #username =  forms.CharField(widget=forms.TextInput(attrs=dict(attrs_dict, maxlength=30)))


    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(attrs_dict, maxlength=30)))

    last_name = forms.CharField(widget=forms.TextInput(attrs=dict(attrs_dict, maxlength=30)))

    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,maxlength=75)),label=_("E-mail"))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),label=_("Password"))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),label=_("Password (again)"))

    
    
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data





    
