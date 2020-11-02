from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TestModel


class MainView(ListView):

    template_name = 'main/models_list.html'
    model = TestModel


class ModelView(DetailView):

    model = TestModel
    template_name = 'main/detail.html'

