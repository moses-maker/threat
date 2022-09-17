from django.urls import re_path, include
from django.contrib import admin, auth

from .views.sdo import sdo_list,sdo_view, sdo_view_recursive
from .views.observables import obs_view
from .views.drs import viz_drs, data_drs
from .views.stix import stix_view ,stix2_json, stix2type_json, stix2_json_masked
from .views.taxii import taxii_discovery, taxii_collection, taxii_get_objects
from .views.timeline import timeline_view
from .views.chart import kill_chain_view, ttp_view, target_chart, actor_chart, chart_view
from .tables import *
#from two_factor.admin import AdminSiteOTPRequired
#from two_factor.urls import urlpatterns as tf_urls

app_name = "strelok_app"
app_name="two_factor"

urlpatterns = [
   
    re_path(r'^account/', include('django.contrib.auth.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^data/attack-pattern/', AttackPatternData.as_view()),
    re_path(r'^data/campaign/', CampaignData.as_view()),
    re_path(r'^data/course-of-action/', CourseOfActionData.as_view()),
    re_path(r'^data/identity/', IdentityData.as_view()),
    re_path(r'^data/intrusion-set/', IntrusionSetData.as_view()),
    re_path(r'^data/malware/', MalwareData.as_view()),
    re_path(r'^data/observed-data/', ObservedDataData.as_view()),
    re_path(r'^data/report/', ReportData.as_view()),
    re_path(r'^data/threat-actor/', ThreatActorData.as_view()),
    re_path(r'^data/tool/', ToolData.as_view()),
    re_path(r'^data/vulnerability/', VulnerabilityData.as_view()),
    re_path(r'^data/relationship/', RelationshipData.as_view()),
    re_path(r'^data/sighting/', SightingData.as_view()),
    re_path(r'^data/indicator/', IndicatorData.as_view()),
    re_path(r'^data/observable/', ObservableObjectData.as_view()),
    re_path(r'^data/pattern/', IndicatorPatternData.as_view()),
    re_path(r'^data/drs/$', data_drs),
    re_path(r'^chart/target/(?P<cnt_by>[a-z]+)$', target_chart),
    re_path(r'^chart/threat-actor/(?P<cnt_by>[a-z]+)$', actor_chart),
    re_path(r'^chart/(?P<id>[a-z\-]+--[0-9a-f\-]+)/(?P<cnt_by>[a-z]+)$', chart_view),
    re_path(r'^stix/$', stix_view),
    re_path(r'^stix/drs/$', viz_drs),
    re_path(r'^stix/matrix/$', ttp_view),
    re_path(r'^stix/matrix/(?P<id>[a-z\-]+--[0-9a-f\-]+)$', ttp_view),
    re_path(r'^stix/(?P<id>[a-z\-]+--[0-9a-f\-]+)\.json$', stix2_json),
    re_path(r'^stix/(?P<id>[a-z\-]+--[0-9a-f\-]+)$', sdo_view),
    re_path(r'^stix/(?P<id>[a-z\-]+--[0-9a-f\-]+)/recursive$', sdo_view_recursive),
    re_path(r'^stix/all.json$', stix2_json),
    re_path(r'^stix/masked-all.json$', stix2_json_masked),
    re_path(r'^stix/(?P<type>[^/]+)\.json$', stix2type_json),
    re_path(r'^stix/(?P<type>[^/]+)', sdo_list),
    re_path(r'^timeline/(?P<id>[a-z\-]+--[0-9a-f\-]+)$', timeline_view),
    re_path(r'^timeline/$', timeline_view),
    re_path(r'^observable/(?P<id>[^/]+)', obs_view),
    re_path(r'^taxii/api/collections/(?P<id>[^/]+)/id/(?P<object_id>[^/]+)/$', taxii_collection),
    re_path(r'^taxii/api/collections/(?P<id>[^/]+)/objects/$', taxii_get_objects),
    re_path(r'^taxii/api/collections/(?P<id>[^/]+)/$', taxii_collection),
    re_path(r'^taxii/api/collections/$', taxii_collection),
    re_path(r'^taxii/$', taxii_discovery),
    re_path(r'^$', viz_drs, name='document_root'),
]
