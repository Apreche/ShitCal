from django.db import models
from django.contrib.auth.models import User

from markitup.fields import MarkupField

class Shit(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    talk = models.BooleanField(default=False)
    description = MarkupField(blank=True)

    class Meta:
        unique_together= (("user", "date"),)
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return u"%s - %s" % (self.user, self.date)
