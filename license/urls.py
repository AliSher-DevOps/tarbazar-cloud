from django.urls import path
from .views import (
    LicenseOrgCreate, LicenseOrgRetrieve,
    LicenseGetCountries, LicenseGetBusinesses,
    LicenseGetCities,  # CheckForSome
)

app_name = 'license'
urlpatterns = [
    # path('', CheckForSome.as_view(), name='org'),

    path('add-org/', LicenseOrgCreate.as_view(), name='add-org'),
    path('get-org/<username>/', LicenseOrgRetrieve.as_view(), name='get-org'),

    path('get-business/', LicenseGetBusinesses.as_view(), name='get-business'),
    path('get-countries/', LicenseGetCountries.as_view(), name='get-countries'),
    path('get-cities/', LicenseGetCities.as_view(), name='get-cities'),
]
