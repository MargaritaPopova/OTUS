import random
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from main.models import Currency, Transaction, Category, Account


class Command(BaseCommand):
    help = 'Work with db'

    models = [Currency, Transaction, Category, Account]
    for model in models:
        model.objects.all().delete()

    def handle(self, *args, **options):
        # Создание
        print('Creating currencies...')
        currencies = ['RUR', 'USD', 'EUR']
        for currency in currencies:
            Currency.objects.create(name=currency)

        print('Creating categories...')
        categories = [
            'Clothing',
            'Tech',
            'Grocery',
            'Pharmacy',
            'Equipment'
        ]
        for category in categories:
            Category.objects.create(name=category)

        print('Creating users...')
        users = [
            {
                'username': 'johnwick',
                'firstname': 'John',
                'lastname': 'Wick',
                'email': 'jw@mail.com',
                'is_staff': 0
            },
            {
                'username': 'brucewayne',
                'firstname': 'Bruce',
                'lastname': 'Wayne',
                'email': 'bw@mail.com',
                'is_staff': 0
            },
            {
                'username': 'jasonbourne',
                'firstname': 'Jason',
                'lastname': 'Bourne',
                'email': 'jb@mail.com',
                'is_staff': 0
            },
            {
                'username': 'jamesbond',
                'firstname': 'James',
                'lastname': 'Bond',
                'email': 'jb7@mail.com',
                'is_staff': 0
            },
        ]
        for user in users:
            User.objects.get_or_create(username=user['username'],
                                       first_name=user['firstname'],
                                       last_name=user['lastname'],
                                       email=user['email'],
                                       is_staff=user['is_staff'])

        print('Creating accounts...')
        for s, curr, usr in list(zip(
                [random.randint(0, 100000) for _ in range(10)],
                [random.choice(Currency.objects.all()) for _ in range(10)],
                [random.choice(User.objects.all()) for _ in range(10)]
        )):
            Account.objects.create(sum=s, currency=curr, user=usr)

        print('Creating transactions...')
        for s, curr, acc, cat in list(zip(
            [random.randint(1, 10000) for _ in range(10)],
            [random.choice(Currency.objects.all()) for _ in range(10)],
            [random.choice(Account.objects.all()) for _ in range(10)],
            [random.choice(Category.objects.all()) for _ in range(10)]
        )):
            Transaction.objects.create(sum=s,
                                       currency=curr,
                                       account=acc,
                                       category=cat)

        print('All data filled in!')
