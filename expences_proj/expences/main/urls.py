from django.urls import path
from .views import \
    CurrencyMainView, \
    CurrencyDetailView, \
    CurrencyListView, \
    CurrencyCreateView, \
    CurrencyDeleteView, \
    CurrencyUpdateView

app_name = 'main'

urlpatterns = [
    path('', CurrencyMainView.as_view(), name='index'),
    path('main/list/', CurrencyListView.as_view(), name='list'),
    path('main/<int:pk>/', CurrencyDetailView.as_view(), name='detail'),
    path('main/create/', CurrencyCreateView.as_view(), name='create'),
    path('main/<int:pk>/update', CurrencyUpdateView.as_view(), name='update'),
    path('main/<int:pk>/delete', CurrencyDeleteView.as_view(), name='delete'),

]
