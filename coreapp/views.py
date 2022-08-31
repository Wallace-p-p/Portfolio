from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import Contact, ContactForm
from django.contrib import messages

# Create your views here.

class MainView(View):
    success_url = reverse_lazy('coreapp:all')
    def get(self, request):
        form = ContactForm()
        ctx = {
            'form': form
        }        
        return render(request, 'coreapp/portfolio.html', ctx)

    def post(self, request, pk=None):
        print(request.POST)
        name = request.POST['name']
        email= request.POST['email']
        message = request.POST['message']
        if len(name)< 60 and len(email) <70 and len(message) < 600:
            contact = Contact(name = name, email= email, message= message)
            contact.save()
            messages.success(request, 'Message submission successful')
            return redirect(self.success_url)
        messages.success(request, 'Message submission Failled due to much caracters, name < 60, email < 70, message < 600')
        return redirect(self.success_url)