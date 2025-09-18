import django_filters
from .models import Paper
class PaperFilter(django_filters.FilterSet):
    min_year = django_filters.NumberFilter(field_name='published_year', lookup_expr='gte')
    max_year = django_filters.NumberFilter(field_name='published_year', lookup_expr='lte')
    author = django_filters.CharFilter(method='filter_author')
    class Meta:
        model = Paper
        fields = ['published_year','author','keywords']
    def filter_author(self, queryset, name, value):
        return queryset.filter(authors__name__icontains=value)
