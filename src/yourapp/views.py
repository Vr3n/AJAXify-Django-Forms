from django.shortcuts import render
from django.views.generic import FormView
from django.http import JsonResponse
from .forms import JoinForm
from .mixins import AjaxFormMixin

# Create your views here.

class JoinFormView(AjaxFormMixin, FormView):
    form_class = JoinForm
    template_name = 'forms/ajax.html'
    success_url = '/form-success/'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email == "abc@gmail.com":
            raise forms.ValidationError("This is not valid")
        return email