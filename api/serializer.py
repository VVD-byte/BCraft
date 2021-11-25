from rest_framework import serializers

from api import models


class CreateStatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StatisticsModel
        fields = '__all__'


class ListStatisticSerializer(serializers.ModelSerializer):
    cpc = serializers.SerializerMethodField()
    cpm = serializers.SerializerMethodField()

    class Meta:
        model = models.StatisticsModel
        fields = '__all__'

    def get_cpc(self, obj):
        return round(obj.Cost/obj.Clicks, 2)

    def get_cpm(self, obj):
        return round(obj.Cost/obj.Views * 1000, 2)
