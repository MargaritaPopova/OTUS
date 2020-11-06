from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Currency


class CurrencyMainView(View):

    template_name = 'main/currency_index.html'

    def get(self, request):
        context = {
            'name': 'This is the main'
        }
        return render(request, self.template_name, context)


class CurrencyListView(ListView):

    model = Currency
    template_name = 'main/currency_list.html'


class CurrencyDetailView(DetailView):

    model = Currency
    template_name = 'main/currency_detail.html'


class CurrencyCreateView(CreateView):
    model = Currency
    fields = ['name']
    success_url = reverse_lazy('main:index')


class CurrencyUpdateView(UpdateView):
    model = Currency
    fields = ['name']
    success_url = reverse_lazy('main:index')


class CurrencyDeleteView(DeleteView):
    model = Currency
    fields = ['name']
    template_name = 'main/currency_confirm_delete.html'
    success_url = reverse_lazy('main:index')


