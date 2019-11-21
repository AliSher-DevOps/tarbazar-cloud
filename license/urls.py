from django.urls import path
from .views import (
    LicenseOrgCreate, LicenseOrgRetrieve,
    LicenseGetCountries, LicenseGetBusinessAll,
    LicenseGetCities, LicenseGetBusinessOne
)

app_name = 'license'
urlpatterns = [

    path('add-org/', LicenseOrgCreate.as_view(), name='add-org'),
    path('get-org/<username>/', LicenseOrgRetrieve.as_view(), name='get-org'),

    path('business-all/', LicenseGetBusinessAll.as_view(), name='business-all'),
    path('business-one/<name>/', LicenseGetBusinessOne.as_view(), name='business-one'),

    path('get-countries/', LicenseGetCountries.as_view(), name='get-countries'),
    path('get-cities/', LicenseGetCities.as_view(), name='get-cities'),
]
