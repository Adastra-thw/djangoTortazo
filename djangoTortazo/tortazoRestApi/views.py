from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from djangoTortazo.tortazoRestApi.tortazoSerializers import UserSerializer, GroupSerializer, ScanSerializer, NodeSerializer, NodePortSerializer
from djangoTortazo.tortazoRestApi.models import  TortazoNode, TortazoScan, TortazoNodePort


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TortazoScanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = TortazoScan.objects.all()
    serializer_class = ScanSerializer

class TortazoNodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = TortazoNode.objects.all()
    serializer_class = NodeSerializer

class TortazoNodePortViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = TortazoNodePort.objects.all()
    serializer_class = NodePortSerializer