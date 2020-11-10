from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from main.models import Account
from main.views import menu


class AccountListView(ListView):

    model = Account
    template_name = 'account/account_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu(self.request)
        return context


class AccountDetailView(DetailView):

    model = Account
    template_name = 'account/account_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu(self.request)
        return context


class AccountCreateView(CreateView):
    model = Account
    fields = '__all__'
    template_name = 'account/account_form.html'
    success_url = reverse_lazy('account:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu(self.request)
        return context


class AccountUpdateView(UpdateView):
    model = Account
    fields = '__all__'
    template_name = 'account/account_form.html'
    success_url = reverse_lazy('account:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu(self.request)
        return context


class AccountDeleteView(DeleteView):
    model = Account
    template_name = 'account/account_confirm_delete.html'
    success_url = reverse_lazy('account:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu(self.request)
        return context


