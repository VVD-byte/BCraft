from rest_framework import serializers

from api import models


class CreateStatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StatisticsModel
        fields = '__all__'


class ListStatisticSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    Date = serializers.DateField()
    cpc = serializers.ReadOnlyField()
    cpm = serializers.ReadOnlyField()

    class Meta:
        model = models.StatisticsModel
        fields = '__all__'
