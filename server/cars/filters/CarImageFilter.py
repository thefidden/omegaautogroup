import django_filters

from cars.models import CarImage


class CarImageFilter(django_filters.FilterSet):
    only_public = django_filters.BooleanFilter(
        method = 'filter_only_public',
        label = 'Только публичные'
    )

    class Meta:
        model = CarImage
        fields = ('only_public',)

    def filter_only_public(self, queryset, name, value):
        if value is True:
            return queryset.filter(public = True)

        return queryset
