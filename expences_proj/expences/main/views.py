# from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import View


def menu(request):
    items = [
        {'name': 'Dashboard',
         'url': '/'},
        {'name': 'Accounts',
         'url': 'account/list'},
        {'name': 'Transactions',
         'url': 'transaction/list'},
    ]

    if request.user.is_authenticated:
        items.extend([
            {'name': 'Profile', 'url': 'profile/'},
            {'name': 'Logout', 'url': reverse_lazy('logout')}
        ])
    else:
        items.extend([
            {'name': 'Login', 'url': reverse_lazy('login')},
            {'name': 'Register', 'url': reverse_lazy('django_registration_register')}
        ])
    return items


class MainView(View):
    template_name = 'main/index.html'

    def get(self, request):
        context = {
            'menu': menu(request),
            'user': request.user if request.user.is_authenticated else None
        }
        return render(request, self.template_name, context)

# class MainLoginView(LoginView):
#     success_url = reverse_lazy('main:index')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = Menu().items
#         return context
