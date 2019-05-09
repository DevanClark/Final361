from django import forms


class CommandForm(forms.Form):
    command = forms.CharField(max_length=300)


class EditUserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    superPermission = forms.BooleanField(required=False)
    adminPermission = forms.BooleanField(required=False)
    instructorPermission = forms.BooleanField(required=False)
    taPermission = forms.BooleanField(required=False)
    address = forms.CharField(max_length=200)
    phonenumber = forms.CharField(max_length=200)
    email = forms.CharField(max_length=30)

    def clean(self):
        cleaned_data = super(EditUserForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        superPermission = cleaned_data.get('superPermission')
        adminPermission = cleaned_data.get('adminPermission')
        instructorPermission = cleaned_data.get('instructorPermission')
        taPermission = cleaned_data.get('taPermission')
        address = cleaned_data.get('address')
        phonenumber = cleaned_data.get('phonenumber')
        email = cleaned_data.get('email')
