from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Currency


class MainView(View):

    template_name = 'main/index.html'

    def get(self, request):
        context = {
            'name': 'This is the main'
        }
        return render(request, self.template_name, context)


class ModelsListView(ListView):

    model = Currency
    template_name = 'main/models_list.html'


class ModelView(DetailView):

    model = Currency
    template_name = 'main/detail.html'

