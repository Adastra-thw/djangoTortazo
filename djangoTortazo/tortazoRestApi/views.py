from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from djangoTortazo.tortazoRestApi.tortazoSerializers import ScanSerializer, NodeSerializer, NodePortSerializer, NodeGeoLocationSerializer, OnionResponsesSerializer, OnionProgressSerializer, BotNodeSerializer, BotNodeGeoLocationSerializer
from djangoTortazo.tortazoRestApi.models import  TortazoNode, TortazoScan, TortazoNodePort,TorNodeGeoLocation, OnionRepositoryResponses, OnionRepositoryProgress, BotNode, BotNodeGeoLocation, ExecutorShodanModel
from django.db.models import Count

from rest_framework import filters

class ScanView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = TortazoScan.objects.all()
    serializer_class = ScanSerializer

class TorNodeView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = TortazoNode.objects.all()
    serializer_class = NodeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('nickname','scanid','id',)

class TorNodePortView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = TortazoNodePort.objects.all()
    serializer_class = NodePortSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('state','tortazonode',)

class TorNodeGeoLocationView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = TorNodeGeoLocation.objects.all()
    serializer_class = NodeGeoLocationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('nodeid',)

class OnionResponsesView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = OnionRepositoryResponses.objects.all()
    serializer_class = OnionResponsesSerializer

class OnionProgressView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = OnionRepositoryProgress.objects.all()
    serializer_class = OnionProgressSerializer


class BotNodeView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = BotNode.objects.all()
    serializer_class = BotNodeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('nickname',)

class BotNodeGeoLocationView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = BotNodeGeoLocation.objects.all()
    serializer_class = BotNodeGeoLocationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('botnodeid',)

'''
class CalcClass(object):

    def __init__(self, *args, **kw):
        # Initialize any variables you need from the input you get
        pass

    def do_work(self):
        # Do some calculations here
        # returns a tuple ((1,2,3, ), (4,5,6,))
        result = ((1,2,3, ), (4,5,6,)) # final result
        return result
'''
class ExecutorShodanView(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request, *args, **kw):
        addressParameter = request.GET.get('address', None)
        shodanModel = ExecutorShodanModel()
        result = shodanModel.searchByHost(addressParameter)
        response = Response(result, status=status.HTTP_200_OK)
        return response        