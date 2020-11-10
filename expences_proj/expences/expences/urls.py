import debug_toolbar
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('account/', include('account.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('transaction/', include('transaction.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]
