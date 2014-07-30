from django.conf.urls import url
from dashboard.views import DashboardIndex
from dashboard.views import DashboardNode

urlpatterns = [
    url(r'^$', DashboardIndex.as_view()),
    url(r'^(?P<id>\d+)/$', DashboardNode.as_view()),
]
