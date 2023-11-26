from django.db import models
from treebeard.mp_tree import MP_Node

"""
    ATR models (Around the Regions, or similar)
"""

class PendingPublication(models.Model):
    publication = models.CharField(
        max_length=64,
        null=False,
        blank=False
    )

    class Meta: 
        db_table = "pending_publication"
        app_label = "mt_tools"
"""
    This table holds the name of the publication
"""

class PendingATREventMaster(models.Model):
    test = models.CharField(
        max_length=24,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "pending_atr_event_master"
        app_label = "mt_tools"

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
        app_label = "mt_tools"

"""
    This table holds the loco, loco_type, 
"""
class PendingATRLocos(models.Model):
    loco_type = models.CharField(
        max_length=3,
        null=False,
        blank=True
    )

    class Meta:
        db_table = "pending_atr_locos"
        app_label = "mt_tools"

