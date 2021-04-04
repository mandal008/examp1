from django import forms


# create forms

class InputForms(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email_id = forms.EmailField(max_length=200)
    phone_no = forms.IntegerField(help_text="Please enter your 10 digit mobile no.")
    password = forms.CharField(widget=forms.PasswordInput())
