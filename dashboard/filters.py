from .models import Course_Materials
import django_filters

class Course_Mat_Filters(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label = 'search')
    class Meta:
        model = Course_Materials
        fields = ['title']