from django.db import models

"""
    This table holds the text and date(s) of the report
"""

class PendingATREventMaster(models.Model):
    test = models.CharField(
        max_length=24,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "pending_atr_event_master"
        app_label = 'mt_tools'

"""
    This table holds the text and date(s) of the report
"""

class PendingATREvent(models.Model):
    test = models.CharField(
        max_length=24,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "pending_atr_event"
        app_label = 'mt_tools'

"""
    This table holds the loco, loco_type, 
"""
class PendingATRLocos(models.Model):
    test = models.CharField(
        max_length=24,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "pendint_atr_locos"
        app_label = 'mt_tools'

