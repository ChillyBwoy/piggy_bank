from django.db import models
from django.utils.translation import ugettext_lazy as _


class Service(models.Model):
    name = models.CharField(_("Имя сервиса"), max_length=60, unique=True, blank=False)
    owners = models.ManyToManyField("accounts.User", through="ServiceOwnership", related_name="services")
    proposals = models.ManyToManyField("accounts.User", through="Proposal", blank=True)

    class Meta:
        verbose_name = _("Сервис")
        verbose_name_plural = _("Сервисы")


__all__ = [
    Service,
]
