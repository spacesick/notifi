from django.db import models

class Period(models.IntegerChoices):
    ONE_MIN = 1
    TEN_MIN = 10
    TWENTY_MIN = 20
    ONE_HOUR = 60