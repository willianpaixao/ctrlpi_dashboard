from django.views.generic import TemplateView
from ctrlpi_xbmc.models import Node

class DashboardIndex(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardIndex, self).get_context_data(**kwargs)
        n = Node.objects.all()
        context['node'] = n
        return context
