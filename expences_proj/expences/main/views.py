from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Currency


class CurrencyMainView(View):

    template_name = 'main/index.html'

    def get(self, request):
        context = {
            'name': 'This is the main'
        }
        return render(request, self.template_name, context)


class  CurrencyListView(ListView):

    model = Currency
    template_name = 'main/currency_list.html'


class CurrencyDetailView(DetailView):

    model = Currency
    template_name = 'main/currency_detail.html'

