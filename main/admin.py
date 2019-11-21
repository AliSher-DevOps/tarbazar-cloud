from django.contrib import admin
from .models import (
    Country, City, PaymentPathway,
    SubModel, SubTime, Subscription,
    Registration, LicenseStatus, License,
    Business, Organization, Frenchise
)


class OrganizationAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    site_header = 'Organization Setup'
    list_display = ('name', 'username', 'isoffcial', 'ismanufecturer', 'iseller')
    search_fields = ('name', 'username', 'email')
    list_filter = ('created',)


admin.site.register(LicenseStatus)
admin.site.register(PaymentPathway)

admin.site.register(Country)
admin.site.register(City)

admin.site.register(SubModel)
admin.site.register(SubTime)
admin.site.register(Subscription)

admin.site.register(Business)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Frenchise)

admin.site.register(License)
admin.site.register(Registration)

admin.site.site_header = 'Tarbazar DevOps'
admin.site.index_title = 'TB - Dashboard'
admin.site.site_title = 'Database'
