from rest_framework import serializers
from djangoTortazo.tortazoRestApi.models import TortazoNode, TortazoNodePort, TortazoScan, OnionRepositoryProgress, OnionRepositoryResponses, BotNode, BotNodeGeoLocation


class ScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TortazoScan
        fields = ('id', 'scandate', 'numnodes')

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
        model = BotNode
        fields = ('partialonionaddress', 'validchars', 'startdate',
                  'enddate', 'progressfirstquartet', 'progresssecondquartet',
                  'progressthirdquartet', 'progressfourthquartet')

class BotNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotNode
        fields = ('nickname', 'userservice', 'password',
                  'address', 'port', 'servicetype')

class BotNodeGeoLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotNodeGeoLocation
        fields = ('botlatitute', 'botlongitute', 'botnodeid')
