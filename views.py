from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from PassValue.forms import HomeForm
# Create your views here.
class HomeView(TemplateView):
    def index(request):
        return render(request, 'home.html')

    def get(self, request):
        form = HomeForm()
        return render(request, 'home.html',{'form':form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            text = form.cleaned_data['post']
            form = HomeForm
            return render(request,'home.html')

        args = {'form': form}
        return render(request, 'home.html', args)