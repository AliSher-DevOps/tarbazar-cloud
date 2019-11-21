from django.urls import path
from .views import (
    LicenseViewCreate_Org, LicenseViewGet_Org,
    LicenseViewGets_Countries, LicenseViewGets_Org,
    LicenseViewGets_City, LicenseViewGet_Business,
    LicenseViewGets_SubModels, LicenseViewGet_SubModels,
    LicenseViewGets_SubTime, LicenseViewGet_SubTime,
    LicenseViewGets_Sub, LicenseViewGet_Sub
)

app_name = 'license'
urlpatterns = [

    path('org/add/', LicenseViewCreate_Org.as_view(), name='org-add'),
    path('org/read/<username>/', LicenseViewGet_Org.as_view(), name='org-read-username'),

    path('business/read/', LicenseViewGets_Org.as_view(), name='business-read'),
    path('business/read/<name>/', LicenseViewGet_Business.as_view(), name='business-read-name'),

    path('country/read/', LicenseViewGets_Countries.as_view(), name='countries-read'),
    path('city/read/', LicenseViewGets_City.as_view(), name='cities-read-country-search'),

    path('submodel/read/', LicenseViewGets_SubModels.as_view(), name='submodel-read'),
    path('submodel/read/<name>', LicenseViewGet_SubModels.as_view(), name='submodel-read-name'),

    path('subtime/read/', LicenseViewGets_SubTime.as_view(), name='subtime-read'),
    path('subtime/read/<name>', LicenseViewGet_SubTime.as_view(), name='subtime-read-name'),

    path('sub/read/', LicenseViewGets_Sub.as_view(), name='sub-read'),
    path('sub/read/<name>', LicenseViewGet_Sub.as_view(), name='sub-read-name'),

]
