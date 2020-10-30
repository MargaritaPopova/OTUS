from django.shortcuts import render
from django.views.generic.base import View
from .models import TestModel


class MainView(View):

    template_name = 'main/index.html'

    def get(self, request):
        for i in range(5):
            t = TestModel.objects.create(name="entry", type=i)
        test_models = TestModel.objects.order_by('id')

        context = {'name': 'Expences app', 'test_models': test_models}
        return render(request, self.template_name, context)
