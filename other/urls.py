from django.urls import path
from .views import (
    CitiesList, SingleCity,
    SingleCityUpdate, SingleCityDelete,
    CityInsert, CityWithCountry,
    CityWithSearch, CityWithUrl,
    BusinessReadAll, BusinessReadOne
)

app_name = 'other'
urlpatterns = [
    path('cities/', CitiesList.as_view()),
    path('city/add/', CityInsert.as_view()),
    path('city/<name>/', SingleCity.as_view(), name='city'),
    path('city/<name>/update/', SingleCityUpdate.as_view(), name='cityupdate'),
    path('city/<name>/delete/', SingleCityDelete.as_view(), name='citydelete'),
    path('city/', CityWithCountry.as_view()),
    path('cityFilter/', CityWithSearch.as_view()),
    path('cit', CityWithUrl.as_view()),

    # ''' REQUIRED AREA TO BE IMPLEMENTED'''
    path('business/', BusinessReadAll.as_view(), name='business-all'),
    path('business/<name>/', BusinessReadOne.as_view(), name='business-one'),
]
