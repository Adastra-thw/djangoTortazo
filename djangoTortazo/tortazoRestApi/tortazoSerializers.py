from django.contrib.auth.models import User, Group
from rest_framework import serializers
from djangoTortazo.tortazoRestApi.models import TortazoNode, TortazoNodePort, TortazoScan


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ScanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TortazoScan
        fields = ('id', 'scanDate')

class NodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TortazoNode
        fields = ('id', 'host','state','reason','nickName','fingerprint','torVersion','contactData','tortazoScan')

class NodePortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TortazoNodePort
        fields = ('id', 'state', 'reason', 'port', 'name', 'version', 'tortazoNode')
