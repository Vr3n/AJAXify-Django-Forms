from django import forms

# Create your forms here.

class JoinForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=120)