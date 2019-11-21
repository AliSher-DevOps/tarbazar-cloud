from rest_framework.serializers import (
    HyperlinkedIdentityField, ModelSerializer
)
from main.models import (
    Organization, Frenchise, Country,
    City, Business, SubModel, SubTime, Subscription
)


# ORGANIZATION -------------------------
class SeriOrganization(ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id', 'name', 'username', 'code',
            'phone', 'email', 'business',
            'address', 'city'
        ]


class SeriFrenchise(ModelSerializer):
    class Meta:
        model = Frenchise
        fields = [
            'name', 'ismain', 'phone', 'email',
            'address', 'city', 'organization'
        ]


# OTHER -----------------------------
class SeriCountries(ModelSerializer):
    class Meta:
        model = Country
        fields = [
            'id', 'name'
        ]


class SerCities(ModelSerializer):
    class Meta:
        model = City
        fields = [
            'id', 'name', 'country'
        ]


class SerBusinesses(ModelSerializer):
    show = HyperlinkedIdentityField(
        view_name='license:business-read-name',
        lookup_field='name'
    )

    class Meta:
        model = Business
        fields = ['id', 'show', 'name', 'desc']


# SUB-SUB>MODEL>TIME --------------
class SerSubModel(ModelSerializer):
    show = HyperlinkedIdentityField(
        view_name='license:submodel-read-name',
        lookup_field='name'
    )

    class Meta:
        model = SubModel
        fields = 'id', 'show', 'name', 'desc'


class SerSubTime(ModelSerializer):
    show = HyperlinkedIdentityField(
        view_name='license:subtime-read-name',
        lookup_field='name'
    )

    class Meta:
        model = SubTime
        fields = 'id', 'show', 'name', 'desc'


class SerSub(ModelSerializer):
    show = HyperlinkedIdentityField(
        view_name='license:sub-read-name',
        lookup_field='name'
    )

    class Meta:
        model = SubTime
        fields = 'id', 'name', 'desc', 'show', 'active'
