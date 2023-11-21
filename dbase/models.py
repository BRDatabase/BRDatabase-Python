from django.db import models
from .models_reference   import RefBuilders, RefOrders, RefCompanies, RefScrapyards
from .models_locomotives import Steam, Diesel, GasTurbine, Electric, DMU, EMU, Railmotor
from .models_allocations import SteamAllocations, DieselAllocations, ElectricAllocations, GasTurbineAllocations, DMUAllocations, EMUAllocations, RailmotorAllocations
