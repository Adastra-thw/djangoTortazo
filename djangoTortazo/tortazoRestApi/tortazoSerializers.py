from rest_framework import serializers
from djangoTortazo.tortazoRestApi.models import TortazoNode, TortazoNodePort, TortazoScan, OnionRepositoryProgress, OnionRepositoryResponses


class ScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TortazoScan
        fields = ('id', 'scandate')

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TortazoNode
        fields = ('id', 'host','state','reason','nickname','fingerprint','torversion','contact','scanid')

class NodePortSerializer(serializers.ModelSerializer):
    class Meta:
        model = TortazoNodePort
        fields = ('id', 'state', 'reason', 'port', 'name', 'version', 'tortazonode')


class OnionResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnionRepositoryResponses
        fields = ('onionaddress', 'responsecode', 'responseheaders', 'oniondescription', 'servicetype')


class OnionProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnionRepositoryProgress
        fields = ('partialonionaddress', 'validchars', 'startdate',
                  'enddate', 'progressfirstquartet', 'progresssecondquartet',
                  'progressthirdquartet', 'progressfourthquartet')
