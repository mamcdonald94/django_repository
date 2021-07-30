from django import forms
from django.forms import fields
from .models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
    # first_name = forms.CharField(max_length=45)
    # last_name = forms.CharField(max_length=45)
    # email = forms.EmailField()
    # password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    # confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

# class RegiFormv2(RegistrationForm):

#     confirm_password = forms.CharField(max_length=55, widget=forms.PasswordInput)

#     class Meta(RegistrationForm.Meta):
#         fields = RegistrationForm.Meta.fields + ('confirm_password',)