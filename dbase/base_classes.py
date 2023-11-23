from lib.enumerated_types import PeriodType
from django.db import models

"""
    The models in this file are not used directly but form the parent class of subsequent classes, specialed into
    steam/diesel/electric/dmu/emu/smu
"""

class BaseAllocations(models.Model):
    loco_id = models.IntegerField(primary_key=True)

    # Build data
    alloc_date = models.DateField(
        null=True,
        blank=True
    )
    
    alloc_prd = models.CharField(
        max_length=2,
        choices=PeriodType.choices,
        null=True,
        blank=True
    )

    # A sequence is required where allocations are made in the same period.
    # Must be part of a unique constraint, along with loco_id and alloc_date
    alloc_sequence = models.SmallIntegerField(
        null=False,
        default=1
    )

    alloc_date = models.DateField(
        null=False,
        blank=False
    )

    # Where did this information come from?
    source = models.TextField(
        null=True,
        blank=True
    )

    class Meta: 
        abstract = True
        app_label = "dbase"

class BaseMotivePower(models.Model):
    loco_id = models.IntegerField(primary_key=True)

    # Build data
    b_date = models.DateField(
        null=True,
        blank=True
    )
    
    b_prd = models.CharField(
        max_length=2,
        choices=PeriodType.choices,
        null=True,
        blank=True
    )
    
    b_notes = models.TextField(
        null=True,
        blank=True
    )
    
    # Withdrawal data
    w_date = models.DateField(
        null=True,
        blank=True
    )
    
    w_prd = models.CharField(
        max_length=2,
        choices=PeriodType.choices,
        null=True,
        blank=True
    )

    w_notes = models.TextField(
        null=True,
        blank=True
    )
    
    # Sold for scrap data
    sfs_date = models.DateField(
        null=True,
        blank=True
    )
    
    sfs_prd = models.CharField(
        max_length=2,
        choices=PeriodType.choices,
        null=True,
        blank=True
    )

    sfs_notes = models.TextField(
        null=True,
        blank=True
    )
    
    # Scrapping data
    s_date = models.DateField(
        null=True,
        blank=True
    )
    
    s_prd = models.CharField(
        max_length=2,
        choices=PeriodType.choices,
        null=True,  
        blank=True
    )

    s_notes = models.TextField(
        null=True,
        blank=True
    )
    
    reason_withdrawn = models.TextField(
        null=True,
        blank=True
    )

    initial_cost = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        null=True,
        blank=True
    )

    initial_cost_notes = models.TextField(
        null=True,
        blank=True
    )

    residual_value = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        null=True,
        blank=True
    )
    
    order_id = models.ForeignKey(
        'RefOrders',
        null=True,
        on_delete=models.SET_NULL
    )

    works_number_a = models.CharField(
        max_length=16,
        null=True,
        blank=True
    )
    
    works_number_b = models.CharField(
        max_length=16,
        null=True,
        blank=True
    )
    
    scrapyard_code = models.ForeignKey(
        'RefScrapyards',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
  
    is_preserved = models.BooleanField(
        null=False,
        default=False
    )

    info = models.TextField(
        null=True,
        blank=True
    )

    # First class data - needs to be overriden by child classes as these are 
    first_class_id = 0
    first_class_var_id = 0

    class Meta: 
        abstract = True
        app_label = "dbase"

class BaseNumbers(models.Model):
    class Meta:
        abstract = True
        app_label = "dbase"
