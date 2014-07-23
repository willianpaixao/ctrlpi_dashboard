from django.conf.urls import url
from dashboard.views import DashboardIndex

urlpatterns = [
    url(r'^$', DashboardIndex.as_view()),
]
