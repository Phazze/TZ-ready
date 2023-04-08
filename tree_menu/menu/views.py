from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView


class MenusViews(TemplateView):
    template_name = 'menu/index.html'

