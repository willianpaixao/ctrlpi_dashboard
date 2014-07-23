from django.views.generic import TemplateView

class DashboardIndex(TemplateView):
    template_name = "index.html"
