from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from djangoTortazo.tortazoRestApi import views

admin.autodiscover()



router = routers.DefaultRouter()

router.register(r'scans', views.ScanView)
router.register(r'scan/torNodeData', views.TorNodeView)
router.register(r'scan/torNodePort', views.TorNodePortView)
router.register(r'scan/geolocation', views.TorNodeGeoLocationView)
router.register(r'repository/responses', views.OnionResponsesView)
router.register(r'repository/incremental', views.OnionProgressView)
router.register(r'botnet/bots', views.BotNodeView)
router.register(r'botnet/locations', views.BotNodeGeoLocationView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^scan/shodan', views.MyRESTView.as_view())
]
