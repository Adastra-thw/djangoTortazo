from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from djangoTortazo.tortazoRestApi import views

admin.autodiscover()



router = routers.DefaultRouter()

router.register(r'scans', views.ScanView)
router.register(r'scan/torNodeData', views.TorNodeView)
router.register(r'scan/torNodePort', views.TorNodePortView)
router.register(r'repository/responses', views.OnionResponsesView)
router.register(r'repository/incremental', views.OnionProgressView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
