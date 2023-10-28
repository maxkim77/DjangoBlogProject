from django.views.generic import TemplateView
class HomeView(TemplateView):
    template_name = 'main/home.html'

class AboutView(TemplateView):
    template_name = 'main/about.html'    
class GeneratorView(TemplateView):
    template_name = 'main/generator.html'    