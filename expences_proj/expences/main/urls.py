from django.urls import path
from .views import CurrencyMainView, CurrencyDetailView, CurrencyListView

app_name = 'main'

urlpatterns = [
    path('', CurrencyMainView.as_view(), name='index'),
    path('main/list/', CurrencyListView.as_view(), name='list'),
    path('main/<int:pk>/', CurrencyDetailView.as_view(), name='detail'),
]
