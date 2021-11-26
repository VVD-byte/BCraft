from rest_framework import serializers

from api import models


class CreateStatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StatisticsModel
        fields = '__all__'


class ListStatisticSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    Date = serializers.DateField()
    cpc = serializers.SerializerMethodField()
    cpm = serializers.SerializerMethodField()

    class Meta:
        model = models.StatisticsModel
        fields = ('id', 'Date', 'Views', 'Clicks', 'Cost', 'cpc', 'cpm')

    def get_cpc(self, obj):
        return round(obj.get('Cost')/obj.get('Clicks'), 2)

    def get_cpm(self, obj):
        return round(obj.get('Cost')/obj.get('Views') * 1000, 2)
