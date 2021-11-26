from rest_framework import generics, response

from api import models, serializer


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

    def get(self, request, *args, **kwargs):
        try:
            response_data = self.serializer_class(
                data=list(self.queryset.filter(
                    Date__gte=request.query_params.get('from'),
                    Date__lt=request.query_params.get('to')
                ).order_by('Date').values()), many=True
            )
            if response_data.is_valid():
                return response.Response(
                    response_data.data
                )
            return response.Response(response_data.errors)
        except Exception as e:
            return super().get(request, *args, **kwargs)


class DropStatisticView(generics.DestroyAPIView):
    """
        Удаляет все записи из модели StatisticsModel
    """
    queryset = models.StatisticsModel.objects.all()

    def delete(self, request, *args, **kwargs):
        self.queryset.delete()
        return response.Response({'drop': True})
