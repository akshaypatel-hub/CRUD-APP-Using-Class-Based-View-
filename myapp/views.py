from django.shortcuts import render ,HttpResponseRedirect
from .forms import ContactForm
from .models import Account

from django.views.generic.edit import  CreateView,UpdateView,DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import  ListView

# Create your views here.
#
# class ContactFormView(FormView):
#     template_name = "home.html"
#     form_class = ContactForm
#     success_url = '/thankyou/'
#
#
#     def form_valid(self, form):
#         print(form.cleaned_data['name'])
#         print(form.cleaned_data['email'])
#         print(form.cleaned_data['msg'])
#         return super().form_valid(form)
#         # return HttpResponseRedirect('/thankyou/')


# List View (Home Page )

class AccountlistView(ListView):
    model = Account
    template_name = "list.html"


# CreateView

class AccountCreateView(CreateView):
    template_name = "account.html"
    model = Account
    fields = '__all__'
    success_url = '/'


    def get_form(self):
        form =super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class' : 'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class' :'myclass'})
        return form

# Detail View

class AccountDetailView(DetailView):
    template_name = "details.html"
    model = Account


# Update View

class AccountUpdateView(UpdateView):
    template_name = "account.html"
    model = Account
    fields = '__all__'
    success_url = '/'

    def get_form(self) :
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class' : 'myclass'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class' : 'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class' : 'myclass'})
        return form

# Delete View

class AccountDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Account
    success_url = '/'


# Thanks Message For  Template View

class ThanksTemplateView(TemplateView):
    template_name = "thanks.html"
