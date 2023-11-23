from django.db import models
from lib.enumerated_types import PeriodType
from .base_classes import BaseAllocations

class SteamAllocations(BaseAllocations):
    class Meta:
        db_table = 's_alloc'

class DieselAllocations(BaseAllocations):
    class Meta:
        db_table = 'd_alloc'

class ElectricAllocations(BaseAllocations):
    class Meta:
        db_table = 'e_alloc'

class GasTurbineAllocations(BaseAllocations):
    class Meta:
        db_table = 'gt_alloc'

class DMUAllocations(BaseAllocations):
    class Meta:
        db_table = 'dmu_alloc'

class EMUAllocations(BaseAllocations):
    class Meta:
        db_table = 'emu_alloc'

class RailmotorAllocations(BaseAllocations):
    class Meta:
        db_table = 'rm_alloc'

