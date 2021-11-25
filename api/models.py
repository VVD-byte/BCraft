from django.db import models


class StatisticsModel(models.Model):
    Date = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    Views = models.IntegerField(verbose_name='Количество показов')
    Clicks = models.IntegerField(verbose_name='Количество кликов')
    Cost = models.FloatField(verbose_name='Стоимость кликов')

    def save(self, *args, **kwargs):
        self.Cost = round(self.Cost, 2)
        return super().save()
