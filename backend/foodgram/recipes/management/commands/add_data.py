import json

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from recipes.models import Ingredient, Tag

User = get_user_model()


class Command(BaseCommand):
    help = 'Наполнить БД тестовыми данными'

    def handle(self, *args, **options):
        data_path = settings.BASE_DIR
        with open(
            f'{data_path}/data/ingredients.json',
            'r',
            encoding='utf-8'
        ) as file:
            reader = json.load(file)
            Ingredient.objects.bulk_create(
                Ingredient(**data) for data in reader
            )
        self.stdout.write(self.style.SUCCESS('Все ингридиенты загружены!'))

        tags_data = [
            {'name': 'Завтрак', 'color': '#E26C2D', 'slug': 'breakfast'},
            {'name': 'Обед', 'color': '#49B64E', 'slug': 'dinner'},
            {'name': 'Ужин', 'color': '#8775D2', 'slug': 'supper'}
        ]
        Tag.objects.bulk_create(Tag(**tag) for tag in tags_data)
        self.stdout.write(self.style.SUCCESS('Все тэги загружены!'))

        users_data = [
            {
                'email': 'admin@admin.ru',
                'username': 'admin',
                'first_name': 'admin',
                'last_name': 'admin',
                'password': make_password('12345'),
                'is_superuser': True,
                'is_staff': True
            },
            {
                'email': 'bingobongo@yamdb.fake',
                'username': 'bingobongo',
                'first_name': 'bingo',
                'last_name': 'bongo',
                'password': make_password('11111')
            },
            {
                'email': 'capt_obvious@yamdb.fake',
                'username': 'capt_obvious',
                'first_name': 'capt',
                'last_name': 'obvious',
                'password': make_password('22222')
            },
            {
                'email': 'faust@yamdb.fake',
                'username': 'faust',
                'first_name': 'faust_first',
                'last_name': 'faust_last',
                'password': make_password('33333')
            },
            {
                'email': 'reviewer@yamdb.fake',
                'username': 'reviewer',
                'first_name': 'reviewer_first',
                'last_name': 'reviewer_last',
                'password': make_password('44444')
            },
            {
                'email': 'angry@yamdb.fake',
                'username': 'angry',
                'first_name': 'angry_first',
                'last_name': 'angry_last',
                'password': make_password('55555')
            }
        ]
        User.objects.bulk_create(User(**users) for users in users_data)
        self.stdout.write(self.style.SUCCESS('Все пользователи загружены!'))
