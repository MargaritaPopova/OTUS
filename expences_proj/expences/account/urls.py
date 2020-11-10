from django.urls import path
from .views import \
    AccountDetailView, \
    AccountListView, \
    AccountCreateView, \
    AccountDeleteView, \
    AccountUpdateView

app_name = 'account'


urlpatterns = [
    path('list/', AccountListView.as_view(), name='list'),
    path('<int:pk>/', AccountDetailView.as_view(), name='detail'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('<int:pk>/update', AccountUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', AccountDeleteView.as_view(), name='delete'),
]
