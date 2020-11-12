from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from main.models import Transaction
from main.views import menu


class TransactionListView(ListView):

    model = Transaction
    template_name = 'transaction/transaction_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu(self.request)
        return context


class TransactionDetailView(DetailView):

    model = Transaction
    template_name = 'transaction/transaction_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu(self.request)
        return context


class TransactionCreateView(CreateView):
    model = Transaction
    fields = '__all__'
    template_name = 'transaction/transaction_form.html'
    success_url = reverse_lazy('transaction:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu(self.request)
        return context


class TransactionUpdateView(UpdateView):
    model = Transaction
    fields = '__all__'
    template_name = 'transaction/transaction_form.html'
    success_url = reverse_lazy('transaction:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu(self.request)
        return context


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'transaction/transaction_confirm_delete.html'
    success_url = reverse_lazy('transaction:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu(self.request)
        return context


