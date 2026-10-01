from django import forms

#class ContactForm(forms.Form):
    #name = forms.CharField(max_length=100, required=True)
    #email = forms.EmailField(required=True)
    #phone = forms.CharField(max_length=15, required=True)
    #message = forms.CharField(widget=forms.Textarea, required=True)





class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': "Name"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': "Email"}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder': "Message", "rows": 5}))





from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
