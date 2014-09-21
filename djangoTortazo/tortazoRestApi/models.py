from django.db import models

# Create your models here.

class TortazoScan(models.Model):
    scandate = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = ('scan')
        verbose_name_plural = ('scan')
        db_table = 'scan'

class TortazoNode(models.Model):
    host = models.CharField(max_length=50)
    state = models.CharField(max_length=6)
    reason = models.CharField(max_length=10)
    #self.openPorts = [] #List of TorNodePort objects
    #self.closedFilteredPorts = [] #List of TorNodePort objects
    nickname = models.CharField(max_length=50)
    fingerprint = models.CharField(max_length=50)
    torversion = models.CharField(max_length=10)
    contact = models.CharField(max_length=40)
    scanid = models.ForeignKey('TortazoScan', db_column='scanid')
    class Meta:
        verbose_name = ('tornodedata')
        verbose_name_plural = ('tornodedata')
        db_table = 'tornodedata'

class TortazoNodePort(models.Model):
    state = models.CharField(max_length=10)
    reason = models.CharField(max_length=10)
    port = models.IntegerField(max_length=6)
    name = models.CharField(max_length=30)
    version = models.CharField(max_length=10)
    tortazonode = models.ForeignKey('TortazoNode', db_column='tornodeid')
    class Meta:
        verbose_name = ('tornodeport')
        verbose_name_plural = ('tornodeport')
        db_table = 'tornodeport'

class OnionRepositoryResponses(models.Model):
    onionaddress = models.CharField(max_length=50)
    responsecode = models.CharField(max_length=4)
    responseheaders = models.CharField(max_length=100)
    oniondescription = models.CharField(max_length=100)
    servicetype = models.CharField(max_length=4)
    class Meta:
        verbose_name = ('onionrepositoryresponses')
        verbose_name_plural = ('onionrepositoryresponses')
        db_table = 'onionrepositoryresponses'

class OnionRepositoryProgress(models.Model):
    partialonionaddress = models.CharField(max_length=10)
    validchars = models.CharField(max_length=10)
    startdate = models.DateTimeField(auto_now=True)
    enddate = models.DateTimeField(auto_now=True)
    #Progress
    progressfirstquartet=models.IntegerField()
    progresssecondquartet=models.IntegerField()
    progressthirdquartet=models.IntegerField()
    progressfourthquartet=models.IntegerField()
    class Meta:
        verbose_name = ('onionrepositoryprogress')
        verbose_name_plural = ('onionrepositoryprogress')
        db_table = 'onionrepositoryprogress'
