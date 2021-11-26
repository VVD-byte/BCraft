import datetime

from django.db import models
from django.core.validators import MinValueValidator


class StatisticsModel(models.Model):
    Date = models.DateField(verbose_name='Дата добавления')
    Views = models.PositiveIntegerField(verbose_name='Количество показов')
    Clicks = models.PositiveIntegerField(verbose_name='Количество кликов')
    Cost = models.FloatField(validators=[MinValueValidator(0.0)], verbose_name='Стоимость кликов')

    @property
    def cpc(self):
        try:
            return round(self.Cost/self.Clicks, 2)
        except:
            return 0

    @property
    def cpm(self):
        try:
            return round(self.Cost/self.Views * 1000, 2)
        except:
            return 0

    def save(self, *args, **kwargs):
        self.Cost = round(self.Cost, 2)
        if self.Date is None:
            self.Date = datetime.datetime.now().date()
        return super().save()
