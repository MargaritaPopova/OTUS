from django.urls import path
from .views import MainView, ModelView

app_name = 'main'

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('main/<int:pk>/', ModelView.as_view(), name='detail'),
]
