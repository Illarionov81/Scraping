from django.db import models
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    name = models.CharField(max_length=32, verbose_name=_("Company"))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')


class Data(models.Model):
    company = models.ForeignKey('webapp.Company', related_name=_("data"), on_delete=models.CASCADE,
                                verbose_name=_("company"))
    date = models.DateField(verbose_name=_("Date"))
    open = models.DecimalField(verbose_name=_("Open"), max_digits=10, decimal_places=6)
    high = models.DecimalField(verbose_name=_("High"), max_digits=10, decimal_places=6)
    low = models.DecimalField(verbose_name=_("Low"), max_digits=10, decimal_places=6)
    close = models.DecimalField(verbose_name=_("Close"), max_digits=10, decimal_places=6)
    adj_close = models.DecimalField(verbose_name=_("Adj Close"), max_digits=10, decimal_places=6)
    volume = models.IntegerField(verbose_name=_("Volume"))

    def __str__(self):
        return f'{self.date}'

    class Meta:
        verbose_name = _('Data')
        verbose_name_plural = _('Data')
