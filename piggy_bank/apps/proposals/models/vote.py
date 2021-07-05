from django.db import models
from django.utils.translation import ugettext_lazy as _


class Vote(models.Model):
    class VoteStatus(models.TextChoices):
        YES = "YES", _("За")
        NO = "NO", _("Против")

    author = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="votes")
    proposal = models.ForeignKey("Proposal", on_delete=models.CASCADE, related_name="votes")
    comment = models.TextField(_("Комментарий"), blank=True)
    status = models.CharField(_("Статус"), max_length=10, choices=VoteStatus.choices)
    created_at = models.DateTimeField(_("Дата создания"), auto_now_add=True)

    class Meta:
        verbose_name = _("Голос")
        verbose_name_plural = _("Голоса")


__all__ = [
    Vote,
]
