from main.models import City, Business
from rest_framework.serializers import (
    ModelSerializer, HyperlinkedIdentityField,
    HyperlinkedModelSerializer
)


class CitiesSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = [
            'id', 'name', 'desc', 'country', 'active'
        ]


class CitiesHyperLinked(ModelSerializer):
    urlshow = HyperlinkedIdentityField(
        view_name='other:city',
        lookup_field='name'
    )
    urlupdate = HyperlinkedIdentityField(
        view_name='other:cityupdate',
        lookup_field='name'
    )
    urldelete = HyperlinkedIdentityField(
        view_name='other:citydelete',
        lookup_field='name'
    )

    class Meta:
        model = City
        fields = [
            'id', 'name', 'desc', 'urlshow',
            'urlupdate', 'urldelete',
        ]


''' REQUIRED AREA TO BE IMPLEMENTED'''


class BusinessSerializer(ModelSerializer):
    urlshow = HyperlinkedIdentityField(
        view_name='other:business-one',
        lookup_field='name'
    )

    class Meta:
        model = Business
        fields = ['id', 'urlshow', 'name', 'desc']
