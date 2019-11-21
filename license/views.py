# REQUIRED-LIBRARIES
# ------------------

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView
)
from main.models import (
    Organization,
    Business, Country, City,
    SubModel, SubTime, Subscription
)
from .serializers import (
    SerCities, SeriCountries, SerBusinesses,
    SeriOrganization, SerSubModel, SerSubTime, SerSub
)
from .bll import LicenseSetup


# ORGANIZATION ----------------------------
class LicenseViewCreate_Org(CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = SeriOrganization

    def perform_create(self, serializer):
        serializer.save()
        LicenseSetup.startfreelicense(data=serializer.data)


class LicenseViewGet_Org(RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = SeriOrganization
    lookup_field = 'username'


class LicenseViewGets_Org(ListAPIView):
    serializer_class = SerBusinesses

    def get_queryset(self):
        queryset_list = Business.objects.all()
        query = self.request.GET.get("ser")
        if query:
            queryset_list = queryset_list.filter(name__icontains=query).distinct()
        return queryset_list


# OTHER ---------------------------------------
class LicenseViewGet_Business(RetrieveAPIView):
    queryset = Business.objects.all()
    serializer_class = SerBusinesses
    lookup_field = 'name'


class LicenseViewGets_Countries(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = SeriCountries


class LicenseViewGets_City(ListAPIView):
    queryset = City.objects.all()
    serializer_class = SerCities

    def get_queryset(self):
        queryset_list = City.objects.all()
        query = self.request.GET.get("ser")
        if query:
            queryset_list = queryset_list.filter(country__name__iexact=query).distinct()
        return queryset_list


# SUB-MODEL ---------------------------------
class LicenseViewGets_SubModels(ListAPIView):
    queryset = SubModel.objects.all()
    serializer_class = SerSubModel


class LicenseViewGet_SubModels(RetrieveAPIView):
    queryset = SubModel.objects.all()
    serializer_class = SerSubModel
    lookup_field = 'name'


# SUB-TIME ---------------------------------
class LicenseViewGets_SubTime(ListAPIView):
    queryset = SubTime.objects.all()
    serializer_class = SerSubTime


class LicenseViewGet_SubTime(RetrieveAPIView):
    queryset = SubTime.objects.all()
    serializer_class = SerSubTime
    lookup_field = 'name'


# SUB-SUB ----------------------------------
class LicenseViewGets_Sub(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SerSub


class LicenseViewGet_Sub(RetrieveAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SerSub
    lookup_field = 'name'


