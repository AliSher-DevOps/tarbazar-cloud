from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter, SearchFilter
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


# class CheckForSome(ListAPIView):
#     queryset = Organization.objects.all()
#     serializer_class = SeriOrganization


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


class LicenseGetBusinesses(ListAPIView):
    queryset = Business.objects.all()
    serializer_class = SerBusinesses


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
