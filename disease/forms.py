from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from .models import User


# class register(forms.ModelForm):
#     class Meta:
#         model = models.SignUpForm
#         fields = ['username','email', 'password1','password2', 'name', 'age', 'contact','city', 'gender']


class UserRegister(UserCreationForm, forms.Form):

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email','password1','password2','gender']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'validate'
            })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email, role=self.instance.role).exclude(username=username).exists():
            raise forms.ValidationError(u'A user with that email address already exists.')
        return email
