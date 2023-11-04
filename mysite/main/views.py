from django.views.generic import TemplateView
class HomeView(TemplateView):
    template_name = 'main/home.html'
class AboutView(TemplateView):
    template_name = 'main/about.html'    
class GeneratorView(TemplateView):
    template_name = 'main/generator.html'    


# TemplateView는 주로 템플릿을 렌더링하여 반환
# Template_name은 속성