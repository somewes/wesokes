from django.views.generic import TemplateView


from django.conf import settings
print settings.STATIC_URL


class IndexView(TemplateView):
    template_name = 'index.html'
