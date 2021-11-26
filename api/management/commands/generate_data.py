import random
import datetime

from django.core.management.base import BaseCommand

from api import models


class Command(BaseCommand):
    help = 'Рандомно заполняет базу StatisticsModel'

    def handle(self, *args, **options):
        count = int(options.get('count', 100))
        for i in range(count):
            date = datetime.datetime.today() - datetime.timedelta(days=random.randint(0, 365))
            obj = models.StatisticsModel(
                Date=date.strftime('%Y-%m-%d'),
                Views=random.randint(1, 10000),
                Cost=random.uniform(1, 100),
            )
            obj.Clicks = random.randint(1, obj.Views)
            obj.save()
        print(f'Созданы {count} случайных записей')

    def add_arguments(self, parser):
        parser.add_argument(
            '-c',
            '--count',
            default=False,
            help='Количество записей'
        )
