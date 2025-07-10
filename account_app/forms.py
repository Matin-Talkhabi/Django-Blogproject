#######################################
# this code could also perform as a form
#######################################


from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_password(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user is not None:
            return self.cleaned_data['password']
        raise ValidationError('username or password is incorrect' , code = 'invalid_password_or_username')


class User_Edit_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']