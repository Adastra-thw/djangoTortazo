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

from core.tortazo.TortazoExecutor import TortazoExecutor
import logging as log
from djangoTortazo.tortazoRestApi.utils.ExecutorUtils import ScanUtils        
import json
        
class ScanView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = TortazoScan.objects.all()
    serializer_class = ScanSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'scandate', 'numnodes','tortazocommand','scanfinished',)

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

class ExecutorTortazoScan(APIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def post(self, request, *args, **kw):
        result = {} 
        try:
            tortazoSwitches = json.loads(request.body)
            
            structure = json.loads(request.body)
            tortazoExecutor = TortazoExecutor(log)
            scanUtils = ScanUtils(tortazoExecutor)

            #First, let's validate the required arguments.
            if scanUtils.validateMandatoryScanArgument(structure) == False:
                result["status"] = "ERROR"
                result["status"] = "Mandatory argument '--mode' not specified."
            else:
                #If the required arguments are set, then validate the values for the optional arguments.
                runable = False
                for argument in structure.keys():
                    if scanUtils.validateScanArgument(structure[argument]) == False:
                        result["status"] = "ERROR"
                        result["status"] = scanUtils.message
                        runable = True
                if runable:
                    self.tortazoExecutor = scanUtils.tortazoExecutor
                    from multiprocessing import Process
                    p = Process(target=tortazoExecutor.run)
                    p.start()           
                    result["status"] = "OK"
                    result["status"] = "Scan started successfully. Wait a few minutes to see the results."
                    #Start a new process for the scan and then, emit the response to the client.
                    #tortazoExecutor.run()        
            
            response = Response(json.dumps(result), status=status.HTTP_200_OK)
            return response        
        except:
            import sys
            result["status"] = "ERROR"
            result["message"] = "Unexpected error: "+str(sys.exc_info)
            response = Response(json.dumps(result), status=status.HTTP_500_OK)
            
