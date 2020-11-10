from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View


class Menu(View):
    items = [
        {'name': 'Dashboard',
         'url': '/'},
        {'name': 'Accounts',
         'url':  'account/list'},
        {'name': 'Transactions',
         'url': 'transaction/list'},
    ]

    def get(self, request):
        if request.user.is_authenticated:
            self.items += [
                {'name': 'Profile',
                 'url': 'profile/'},
                {'name': 'Logout',
                 'url': '/'}
            ]
        else:
            self.items += [{
                'name': 'Login',
                'url': '/'
            }]


class MainView(View):
    template_name = 'main/index.html'

    def get(self, request):
        context = {
            'menu': Menu().items,
        }
        return render(request, self.template_name, context)
