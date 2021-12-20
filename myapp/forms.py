from django import forms



class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)