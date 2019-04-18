from django import forms

class CommandForm(forms.Form):
    command = forms.CharField(max_length=300)

class EditUserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    permissions = forms.CharField(max_length=20)

    address = forms.CharField(max_length=200)
    phonenumber = forms.CharField(max_length=200)
    email = forms.CharField(max_length=30)

