from django.shortcuts import render
from django.views.generic.base import View


class MainView(View):

    template_name = 'main/index.html'

    def get(self, request):
        context = {'name': 'Expences app'}
        return render(request, self.template_name, context)
