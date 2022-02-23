import datetime

from django.db import models


class TSFieldsIndexed(models.Model):
    ts_created = models.DateTimeField(default=datetime.datetime.now(), db_index=True, editable=True)
    ts_updated = models.DateTimeField(auto_now=True, db_index=True, editable=True)

    class Meta:
        abstract = True


class TimeFields(models.Model):
    ts_created = models.DateTimeField(default=datetime.datetime.now(), editable=False)
    ts_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
