from django.db import models

# Create your models here.

class Lending(models.Model):
    checkout_date = models.DateField(verbose_name="貸出日", null=True)
    return_date = models.DateField(verbose_name="返却日", null=True)
    overdue = models.BooleanField(verbose_name="返却日超過", default=False)
