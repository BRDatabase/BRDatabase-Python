from typing import Any
from django.http import HttpResponse
from django.views.generic import TemplateView

app_name = 'home'

class SitesHomePage(TemplateView):
    
    template_name = "sites.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['data'] = "Context Data"

        return context