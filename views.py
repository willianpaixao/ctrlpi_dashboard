from django.shortcuts import render
from django.views.generic import TemplateView
from ctrlpi_xbmc.models import Node

class DashboardIndex(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardIndex, self).get_context_data(**kwargs)
        n = Node.objects.all()
        context[u"node"] = n
        return context

class DashboardNode(TemplateView):
    template_name = "node.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardNode, self).get_context_data(**kwargs)
        i = int(self.kwargs["id"])
        context[u"node"] = Node.objects.get(pk=i)
        return context

