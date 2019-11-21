from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
    UpdateAPIView, DestroyAPIView,
    CreateAPIView
)
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from .pagination import PostLimitOddsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from main.models import City, Business
from .Serializers import CitiesSerializer, CitiesHyperLinked, BusinessSerializer


class CityInsert(CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitiesSerializer


# Only get method allowed here in this case [all]
class CitiesList(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitiesSerializer


# Only get method is allowed but [single]
class SingleCity(RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitiesSerializer
    lookup_field = 'name'
    # lookup_url_kwarg = 'names'
    # OPTIONAL WHEN lookup_field not same to URLATTRIB


class SingleCityUpdate(UpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CitiesSerializer
    lookup_field = 'name'


class SingleCityDelete(DestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitiesSerializer
    lookup_field = 'name'


class CityWithCountry(ListAPIView):
    serializer_class = CitiesSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'name', 'country__name']
    pagination_class = LimitOffsetPagination  # http://127.0.0.1:8000/other/city/?limit=2

    def get_queryset(self, *args, **kwargs):
        queryset_list = City.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(country__name=query).distinct()
        return queryset_list


class CityWithSearch(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitiesSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'name', 'country__name']
    pagination_class = PostLimitOddsetPagination


class CityWithUrl(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitiesHyperLinked


''' REQUIRED AREA TO BE IMPLEMENTED'''


class BusinessReadOne(RetrieveAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    lookup_field = 'name'


class BusinessReadAll(ListAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

