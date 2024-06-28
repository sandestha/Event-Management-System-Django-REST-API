from django.db import models
from base.models import Events, Vendors
# Create your models here.

class Catering(models.Model):
    catering_detail = models.CharField(max_length=300,default='')
    event = models.ForeignKey(Events,on_delete=models.SET_NULL,null=True)
    vendor_name = models.ForeignKey(Vendors,on_delete=models.SET_NULL,null=True)
    cost = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Catering'

    def __str__(self):
        return self.catering_detail


class Equipment(models.Model):
    equipment_detail = models.CharField(max_length=300,default='')
    event = models.ForeignKey(Events,on_delete=models.SET_NULL,null=True)
    vendor_name = models.ForeignKey(Vendors,on_delete=models.SET_NULL,null=True)
    cost = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Equipment'

    def __str__(self):
        return self.equipment_detail

class Transportation(models.Model):
    transport_detail = models.CharField(max_length=300,default='')
    event = models.ForeignKey(Events,on_delete=models.SET_NULL,null=True)
    vendor_name = models.ForeignKey(Vendors,on_delete=models.SET_NULL,null=True)
    cost = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Transportation'

    def __str__(self):
        return self.transport_detail
