from django.utils.translation import gettext_lazy as _
from django.db import models

class PeriodType(models.TextChoices):
    PRD_DAY = "E", _("Exact")
    PRD_WEEK = "1W", _("Week Ending")
    PRD_2_WEEKS = "2W", _("2 Week Ending")
    PRD_3_WEEKS = "3W", _("3 Week Ending")
    PRD_4_WEEKS = "4W", _("4 Week Ending")
    PRD_MONTH = "1M", _("Month Ending")
    PRD_2_MONTHS = "2M", _("2 Month Ending")
    PRD_3_MONTHS = "3M", _("3 Month Ending")
    PRD_4_MONTHS = "4M", _("4 Month Ending")
    PRD_5_MONTHS = "5M", _("5 Month Ending")
    PRD_6_MONTHS = "6M", _("6 Month Ending")
    PRD_ANNUAL = "1Y", _("Year Ending")


class AllocationFlags(models.TextChoices):
    ALLOC_NEW = "N", _("New")
    ALLOC_CONDEMNED = "C", _("Condemned") # final withdrawal
    ALLOC_WITHDRAWN = "W", _("Withdrawn") # Used when subsequently reinstated
    ALLOC_STORED = "S", _("Stored")
    ALLOC_REINSTATED = "R", _("Reinstated")
    ALLOC_DUMPED = "D", _("Dumped")
    ALLOC_HIRE = "H", _("On Hire")
    ALLOC_LOAN = "L", _("On Loan")
    ALLOC_BACK = "B", _("Returned from Loan/Hire")
    ALLOC_STOCK = "K", _("New to Stock")
