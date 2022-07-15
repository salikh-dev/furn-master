from django.views import generic
from django.shortcuts import render

class Home(generic.TemplateView):
    template_name = "dashboard/pages/index.html"


class Btns(generic.TemplateView):
    template_name = 'dashboard/pages/btns.html'
    
class Cards(generic.TemplateView):
    template_name = "dashboard/pages/card.html"

class Blank(generic.TemplateView):
    template_name = "dashboard/pages/blank.html"

class Colors(generic.TemplateView):
    template_name = "dashboard/pages/colors.html"

class Borders(generic.TemplateView):
    template_name = "dashboard/pages/borders.html"

class Animations(generic.TemplateView):
    template_name = "dashboard/pages/animations.html"

class Others(generic.TemplateView):
    template_name = "dashboard/pages/others.html"