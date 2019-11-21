from main.models import (
    Frenchise, City, Organization,
    Subscription, Registration,
    PaymentPathway, License, LicenseStatus
)
from datetime import date, datetime


class LicenseSetup:

    @staticmethod
    def startfreelicense(data):
        city = City.objects.get(pk=data['city'])
        organization = Organization.objects.get(pk=data['id'])

        subscription = Subscription.objects.get(name__iexact='starter-premium')
        pathway = PaymentPathway.objects.get(name__iexact='free')
        status = LicenseStatus.objects.get(name__iexact='active')

        frenshiseset = Frenchise(
            name=data['name'],
            ismain=True,
            email=data['email'],
            phone=data['phone'],
            address=data['address'],
            city=city,
            organization=organization
        ).save()

        licenseset = License(
            organization=organization,
            licensestatus=status
        ).save()

        registrationset = Registration(
            subscription=subscription,
            organization=organization,
            pathway=pathway,
            ends=datetime(2020, 3, 31),
        ).save()
