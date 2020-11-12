from django.urls import path
from .views import \
    TransactionDetailView, \
    TransactionListView, \
    TransactionCreateView, \
    TransactionDeleteView, \
    TransactionUpdateView

app_name = 'transaction'


urlpatterns = [
    path('list/', TransactionListView.as_view(), name='list'),
    path('<int:pk>/', TransactionDetailView.as_view(), name='detail'),
    path('create/', TransactionCreateView.as_view(), name='create'),
    path('<int:pk>/update', TransactionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', TransactionDeleteView.as_view(), name='delete'),
]
