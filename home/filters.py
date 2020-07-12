import django_filters
from home.models import SearchHistory

class SearchFilter(django_filters.FilterSet):
    class Meta:
        model = SearchHistory
        fields = [
            'loginuser',
            'keyword',
            'searchdate',
            'searchresult',
        ]