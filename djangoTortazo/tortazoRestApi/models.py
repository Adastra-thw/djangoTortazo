from django.db import models

# Create your models here.

class TortazoScan(models.Model):
    scanDate = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = ('scan')
        verbose_name_plural = ('scan')

class TortazoNode(models.Model):
    host = models.CharField(max_length=50)
    state = models.CharField(max_length=6)
    reason = models.CharField(max_length=10)
    #self.openPorts = [] #List of TorNodePort objects
    #self.closedFilteredPorts = [] #List of TorNodePort objects
    nickName = models.CharField()
    fingerprint = models.CharField()
    torVersion = models.CharField(max_length=10)
    contactData = models.CharField(max_length=40)
    tortazoScan = models.ForeignKey('TortazoScan')
    class Meta:
        verbose_name = ('node')
        verbose_name_plural = ('node')

class TortazoNodePort(models.Model):
    state = models.CharField()
    reason = models.CharField()
    port = models.IntegerField()
    name = models.CharField(max_length=30)
    version = models.CharField(max_length=10)
    tortazoNode = models.ForeignKey('TortazoNode')
    class Meta:
        verbose_name = ('nodePort')
        verbose_name_plural = ('nodePort')