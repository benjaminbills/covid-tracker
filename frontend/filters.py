import django_filters
from address.models import Address
from django_filters import DateFilter, CharFilter
class AddressFilter(django_filters.FilterSet):
  name = CharFilter(field_name='name', lookup_expr='icontains')
  address = CharFilter(field_name='address', lookup_expr='icontains')
  date_from = DateFilter(field_name='date', lookup_expr='gte')
  date_to = DateFilter(field_name='date', lookup_expr='lte')
  class Meta:
    model = Address
    fields = 'name','address', 
    