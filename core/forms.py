from django import forms
from .models import Cricketer, collect_img
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CricketerForm(forms.ModelForm):    
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d']  # Accepts YYYY-MM-DD format
    )
    
    class Meta:
        model = Cricketer
        fields = '__all__'

class collect_img_Form(forms.ModelForm):
    class Meta:
        model = collect_img
        fields = ('name', 'image', 'file')

class registration_Form(UserCreationForm):
    email = forms.EmailField(required=True) 
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')