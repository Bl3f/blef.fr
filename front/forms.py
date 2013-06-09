from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.CharField(required=False)
    message = forms.CharField()