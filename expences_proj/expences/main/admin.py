from django.contrib import admin
from .models import Currency, Transaction, Account, Category

admin.site.register(Currency)
admin.site.register(Transaction)
admin.site.register(Account)
admin.site.register(Category)
