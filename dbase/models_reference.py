from django.db import models
from lib.enumerated_types import PeriodType
from .custom_fields import LocationField

class RefOrders(models.Model):
    stub_name = 'RefOrders_'

    order_id = models.IntegerField(
        primary_key=True
    )

    class Meta:
        app_label = "dbase"
        db_table = "ref_orders"

class RefScrapyards(models.Model):
    stub_name = 'RefScrapyards_'

    scrapyard_code = models.CharField(
        max_length=5,
        primary_key=True
    )

    class Meta:
        app_label = "dbase"
        db_table = "ref_scrapyards"

class RefCompanies(models.Model):
    stub_name = 'RefCompanies_'

    company_id = models.IntegerField(
        primary_key=True
    )
    
    class Meta:
        app_label = "dbase"
        db_table = "ref_companies"

class RefBuilders(models.Model):
    stub_name = 'RefBuilders_'

    bl_code = models.CharField(
        max_length=4,
        primary_key=True
    )

    bl_name = models.CharField(
        max_length=128,
        null=False,
        blank=False
    )

    bl_shortened_name = models.CharField(
        max_length=24,
        null=True,
        blank=True,
    )

    # Field to hold latitude and longitude
    location = LocationField(
    )

    opened_date = models.DateField(
        null=True,
        blank=True
    )

    closed_date = models.DateField(
        null=True,
        blank=True
    )

    closure_reason = models.TextField(
        null=True,
        blank=True
    )

    prg = models.ForeignKey(
        'RefCompanies',
        null=True,
        related_name=stub_name + 'prg',
        on_delete=models.SET_NULL
    )

    big4 = models.ForeignKey(
        'RefCompanies',
        null=True,
        related_name=stub_name + 'big4',
        on_delete=models.SET_NULL
    )

    class Meta:
        app_label = "dbase"
        db_table = "ref_builders"

