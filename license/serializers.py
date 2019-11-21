from rest_framework.serializers import (
    HyperlinkedIdentityField, ModelSerializer
)
from main.models import (
    Organization, Frenchise, Country,
    City, Business
)


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
        view_name='license:business-one',
        lookup_field='name'
    )

    class Meta:
        model = Business
        fields = ['id', 'show', 'name', 'desc']
