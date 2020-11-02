from django.urls import path
from .views import MainView, ModelView, ModelsListView

app_name = 'main'

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('main/list/', ModelsListView.as_view(), name='list'),
    path('main/<int:pk>/', ModelView.as_view(), name='detail'),
]
