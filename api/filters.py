from django_filters import FilterSet, NumberFilter, DateFilter

from api import models


class StatisticsFilter(FilterSet):

    from_ = DateFilter(field_name="Date", lookup_expr='gte')
    to = DateFilter(field_name="Date", lookup_expr='lt')

    class Meta:
        model = models.StatisticsModel
        fields = ['from_', 'to', 'id', 'Views', 'Clicks', 'Cost']
