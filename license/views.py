from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView
)
from main.models import (
    Organization, Frenchise, Business,
    Country, City
)
from .serializers import (
    SerCities, SeriCountries, SerBusinesses,
    SeriOrganization, SeriFrenchise
)
from .bll import LicenseSetup


class LicenseOrgCreate(CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = SeriOrganization

    def perform_create(self, serializer):
        serializer.save()
        LicenseSetup.startfreelicense(data=serializer.data)


class LicenseOrgRetrieve(RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = SeriOrganization
    lookup_field = 'username'


class LicenseGetBusinessAll(ListAPIView):
    serializer_class = SerBusinesses

    def get_queryset(self):
        queryset_list = Business.objects.all()
        query = self.request.GET.get("ser")
        if query:
            queryset_list = queryset_list.filter(name__icontains=query).distinct()
        return queryset_list


class LicenseGetBusinessOne(RetrieveAPIView):
    queryset = Business.objects.all()
    serializer_class = SerBusinesses
    lookup_field = 'name'


class LicenseGetCountries(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = SeriCountries


class LicenseGetCities(ListAPIView):
    queryset = City.objects.all()
    serializer_class = SerCities

    def get_queryset(self):
        queryset_list = City.objects.all()
        query = self.request.GET.get("country")
        if query:
            queryset_list = queryset_list.filter(country__name__iexact=query).distinct()
        return queryset_list
