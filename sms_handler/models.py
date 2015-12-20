from django.db import models


class ApiLog(models.Model):
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    msg = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.created
