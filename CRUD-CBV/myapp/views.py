from django.shortcuts import render,redirect,HttpResponseRedirect

from .forms import StudentRegistration
from .models import Student
from django.views.generic.base import TemplateView , RedirectView , View

# Create your views here.


# This class will be add item and show all item in page

class homeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self,*args ,**kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        obj = Student.objects.all()
        context = {"form":fm,"obj":obj}
        return context

    def post(self,request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/home')


# This class will be Edit item 

class UpdateView(View):

    def get(self,request,pk):

        frm = Student.objects.get(pk=pk)
        fm= StudentRegistration(request.POST , instance=frm)
        return HttpResponseRedirect('/home')

    def post(self,request,pk):
        frm = Student.objects.get(pk=pk)
        fm = StudentRegistration(request.POST, instance=frm)
        if fm.is_valid():
            fm.save()
        return render(request, "update.html", {"form" : fm})




# # This class will be Delete item 

class DeleteView(RedirectView):
    url = '/home'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['pk']
        Student.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args , **kwargs)

