from django.db import models
from lib.enumerated_types import PeriodType
from .base_classes import BaseMotivePower

"""
    Locomotives and multiple units/railmotor tables all inherit much of their information
    but some is specific to each.
"""

class Steam(BaseMotivePower):
    
    stub_name = 'steam_'
    
    """
        I don't like this but I have had to move these two fields out of the base class because
        I am getting a reverse accessor error where every child model has the same related_name,
        so by moving them into these subclasses, I can specify the related_name explicitly. If I
        a better way to do this I will change it.
    """

    builder_id = models.ForeignKey( 
        'RefBuilders',
        null=True,
        on_delete=models.SET_NULL,
        related_name=stub_name + 'builder'
    )

    subbuilder_id = models.ForeignKey(
        'RefBuilders',
        null=True,
        on_delete=models.SET_NULL,
        related_name=stub_name + 'subbuilder'
    )

    """
        Steam locomotives often have extra data referring to it's withdrawal. 
        The following three fields are related to that extra informatiion
    """
    w_order = models.CharField(
        max_length=24,
        null=True,
        blank=True
    )

    w_authority = models.CharField(
        max_length=24,
        null=True,
        blank=True
    )

    w_authority_date = models.DateField(
        null=True,
        blank=True
    )

    w_authority_prd = models.CharField(
        max_length=2,
        choices=PeriodType.choices,
        null=True,
        blank=True
    )

    """
        The next pair of fields relate to the date the locomotive was taken into the works for scrapping.
        This data usually comes from the Yeadon books but may be available on the National Archives history cards.
    """
    into_works_for_scrapping_date = models.DateField(
        null=True,
        blank=True
    )

    into_works_for_scrapping_prd = models.CharField(
        max_length=2,
        choices=PeriodType.choices,
        null=True,
        blank=True
    )

    """
        These two fields refer to the number allocated by Crewe Works to some locomotives on scrapping.
        The second field may also be used for any kind of anecdote associated with the scrapping of this
        locomotive.
    """
    cut_number = models.CharField(
        max_length=12,
        null=True,
        blank=True
    )

    cut_notes = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = 's_locomotive'

class Diesel(BaseMotivePower):

    stub_name = 'diesel_'

    """
        I don't like this but I have had to move these two fields out of the base class because
        I am getting a reverse accessor error where every child model has the same related_name,
        so by moving them into these subclasses, I can specify the related_name explicitly. If I
        a better way to do this I will change it.
    """

    builder_id = models.ForeignKey( 
        'RefBuilders',
        null=True,
        on_delete=models.SET_NULL,
        related_name=stub_name + 'builder'
    )

    subbuilder_id = models.ForeignKey(
        'RefBuilders',
        null=True,
        on_delete=models.SET_NULL,
        related_name=stub_name + 'subbuilder'
    )

    class Meta:
        db_table = 'd_locomotive'

class GasTurbine(BaseMotivePower):
    stub_name = 'gasturbine_'

    """
        I don't like this but I have had to move these two fields out of the base class because
        I am getting a reverse accessor error where every child model has the same related_name,
        so by moving them into these subclasses, I can specify the related_name explicitly. If I
        a better way to do this I will change it.
    """

    builder_id = models.ForeignKey( 
        'RefBuilders',
        null=True,
        on_delete=models.SET_NULL,
        related_name=stub_name + 'builder'
    )

    subbuilder_id = models.ForeignKey(
        'RefBuilders',
        null=True,
        on_delete=models.SET_NULL,
        related_name=stub_name + 'subbuilder'
    )

    class Meta:
        db_table = 'gt_locomotive'

class Electric(BaseMotivePower):
    stub_name = 'electric_'

    """
        I don't like this but I have had to move these two fields out of the base class because
        I am getting a reverse accessor error where every child model has the same related_name,
        so by moving them into these subclasses, I can specify the related_name explicitly. If I
        a better way to do this I will change it.
    """

    builder_id = models.ForeignKey( 
        'RefBuilders',
        null=True,
        on_delete=models.SET_NULL,
        related_name=stub_name + 'builder'
    )

    subbuilder_id = models.ForeignKey(
        'RefBuilders',
        null=True,
        on_delete=models.SET_NULL,
        related_name=stub_name + 'subbuilder'
    )
    class Meta:
        db_table = 'e_locomotive'

class DMU(BaseMotivePower):
    stub_name = 'dmu_'

    """
        I don't like this but I have had to move these two fields out of the base class because
        I am getting a reverse accessor error where every child model has the same related_name,
        so by moving them into these subclasses, I can specify the related_name explicitly. If I
        a better way to do this I will change it.
    """

    builder_id = models.ForeignKey( 
        'RefBuilders',
        null=True,
        on_delete=models.SET_NULL,
        related_name=stub_name + 'builder'
    )

    subbuilder_id = models.ForeignKey(
        'RefBuilders',
        null=True,
        on_delete=models.SET_NULL,
        related_name=stub_name + 'subbuilder'
    )

    class Meta:
        db_table = 'dmu_vehicle'

class EMU(BaseMotivePower):
    stub_name = 'emu_'

    """
        I don't like this but I have had to move these two fields out of the base class because
        I am getting a reverse accessor error where every child model has the same related_name,
        so by moving them into these subclasses, I can specify the related_name explicitly. If I
        a better way to do this I will change it.
    """

    builder_id = models.ForeignKey( 
        'RefBuilders',
        null=True,
        on_delete=models.SET_NULL,
        related_name=stub_name + 'builder'
    )

    subbuilder_id = models.ForeignKey(
        'RefBuilders',
        null=True,
        on_delete=models.SET_NULL,
        related_name=stub_name + 'subbuilder'
    )

    class Meta:
        db_table = 'emu_vehicle'

class Railmotor(BaseMotivePower):
    stub_name = 'railmotor_'

    """
        I don't like this but I have had to move these two fields out of the base class because
        I am getting a reverse accessor error where every child model has the same related_name,
        so by moving them into these subclasses, I can specify the related_name explicitly. If I
        a better way to do this I will change it.
    """

    builder_id = models.ForeignKey( 
        'RefBuilders',
        null=True,
        on_delete=models.SET_NULL,
        related_name=stub_name + 'builder'
    )

    subbuilder_id = models.ForeignKey(
        'RefBuilders',
        null=True,
        on_delete=models.SET_NULL,
        related_name=stub_name + 'subbuilder'
    )

    class Meta:
        db_table = 'rm_vehicle'
