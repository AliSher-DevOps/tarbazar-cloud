from django.db import models


# => REQUIRED MODULES
class Country(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    desc = models.TextField(null=True, blank=True)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    desc = models.TextField(null=True, blank=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


# => LICENSE MODULE
class PaymentPathway(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    desc = models.TextField(null=True, blank=True)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural = 'Payment Pathways'

    def __str__(self):
        return self.name


class SubModel(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    desc = models.TextField(null=True, blank=True)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural = 'Subscription Models'

    def __str__(self):
        return self.name


class LicenseStatus(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False ,unique=True)
    desc = models.TextField(null=True, blank=True)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural = 'License Status'

    def __str__(self):
        return self.name


class SubTime(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    desc = models.TextField(null=True, blank=True)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural = 'Subscription Time'

    def __str__(self):
        return self.name


class Subscription(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    desc = models.TextField(null=True, blank=True)
    submodel = models.ForeignKey(SubModel, on_delete=models.CASCADE)
    subtype = models.ForeignKey(SubTime, on_delete=models.CASCADE)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural = 'Subscriptions'

    def __str__(self):
        return self.name


class Registration(models.Model):
    subscription = models.ForeignKey('Subscription', on_delete=models.CASCADE)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    pathway = models.ForeignKey('PaymentPathway', on_delete=models.SET_DEFAULT, default='Free')

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    ends = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return F"{self.organization.name} Subscribed on {self.created}"

    class Meta:
        verbose_name_plural = 'Registrations'


class License(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    licensestatus = models.ForeignKey('LicenseStatus', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    udpated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Licenses'

    def __str__(self):
        return f"License {self.id} issued to {self.organization.name}"


# => ORGANIZATION MODULES
class Business(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    desc = models.TextField(null=True, blank=True)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural = 'Businesses'

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    username = models.TextField(null=False, blank=False, unique=True)
    code = models.TextField(max_length=100, blank=True, null=True)
    isoffcial = models.BooleanField(default=False, null=False)
    ismanufecturer = models.BooleanField(default=False, null=True, blank=True)
    iseller = models.BooleanField(default=True, null=True, blank=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(null=False, blank=False)
    logo = models.ImageField(upload_to='images/', null=True, blank=True)
    banner = models.ImageField(upload_to='images/', null=True, blank=True)
    business = models.ForeignKey('Business', on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=False, blank=False, default='unknown')
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural = 'Organizations'

    def __str__(self):
        return self.name


class Frenchise(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    ismain = models.BooleanField(default=True, null=False, blank=False)
    phone = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False, default='unknown')
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural = 'Frenchises'

    def __str__(self):
        return self.name
