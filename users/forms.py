from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # NOhila's  CODE
    First_name = forms.CharField(max_length=30, required=True)
    Last_name = forms.CharField(max_length=30, required=True)
    Studies = forms.CharField(max_length=9, required=True, help_text='Are you studying at INPT,if (yes) write whitch year.')
    Field = forms.CharField(max_length=20, required=False, help_text='Your current field or the one you are used to be in at INPT.')
    Birthday = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    
    
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']        



class ProfileUpdateForm(forms.ModelForm):

    class Meta:
    	model = Profile
    	fields = ['image']