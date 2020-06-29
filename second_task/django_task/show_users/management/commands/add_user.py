from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Создание пользователя'

    def add_arguments(self, parser):
        parser.add_argument('login', help='Имя пользователя')
        parser.add_argument('password', help='Пароль пользователя')

    def handle(self, *args, **kwargs):
        login = kwargs['login']
        password = kwargs['password']
        User.objects.create_user(username=login, email='', password=password)
