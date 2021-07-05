from django.db import models
from django.utils.translation import ugettext_lazy as _


class Proposal(models.Model):
    class ProposalStatus(models.TextChoices):
        PENDING = "PENDING", _("Ожидает рассмотрения")
        APPROVED = "APPROVED", _("Подтверждено")
        REJECTED = "REJECTED", _("Отклонено")

    service = models.ForeignKey("Service", on_delete=models.CASCADE, related_name="ownership")
    author = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="proposals")
    description = models.TextField(_("Описание"), blank=False)
    status = models.CharField(
        _("Статус"), max_length=30, choices=ProposalStatus.choices, default=ProposalStatus.PENDING
    )
    created_at = models.DateTimeField(_("Дата создания"), auto_now_add=True)

    class Meta:
        verbose_name = _("Предложение")
        verbose_name_plural = _("Предложения")


__all__ = [
    Proposal,
]
