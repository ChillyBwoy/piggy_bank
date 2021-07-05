from django.db import models
from django.utils.translation import ugettext_lazy as _


class ServiceOwnership(models.Model):
    class ServiceOwnershipRole(models.TextChoices):
        ROOT = "ROOT", _("Батя")
        DEVELOPER = "DEVELOPER", _("Разработчик")
        INNER_USER = "INNER_USER", _("Внутренний пользователь")
        OUTER_USER = "OUTER_USER", _("Внешний пользователь")

    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    service = models.ForeignKey("Service", on_delete=models.CASCADE)
    role = models.CharField(_("Роль"), max_length=20, choices=ServiceOwnershipRole.choices)


__all__ = [
    ServiceOwnership,
]
