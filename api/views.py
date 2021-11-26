from rest_framework import generics, response
from django_filters.rest_framework import DjangoFilterBackend

from api import models, serializer, filters


class CreateStatisticView(generics.CreateAPIView):
    """
        Создает записть в модели StatisticsModel
        :param  date - дата события
                views - количество показов
                clicks - количество кликов
                cost - стоимость кликов (в рублях с точностью до копеек)
        :return Данные созданной записи
    """
    queryset = models.StatisticsModel.objects.all()
    serializer_class = serializer.CreateStatisticSerializer


class ListStatisticView(generics.ListAPIView):
    """
        Выводит записи из модели StatisticsModel
        :param  from - дата начала периода (включительно)
                to - дата окончания периода (включительно)
        :return Записи отфильтрованные по вермени
    """
    queryset = models.StatisticsModel.objects.all()
    serializer_class = serializer.ListStatisticSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = filters.StatisticsFilter


class DropStatisticView(generics.DestroyAPIView):
    """
        Удаляет все записи из модели StatisticsModel
    """
    queryset = models.StatisticsModel.objects.all()

    def delete(self, request, *args, **kwargs):
        self.queryset.delete()
        return response.Response({'drop': True})
