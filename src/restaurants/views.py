from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
import random

# Create your views here


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        num=None
        some_list= [random.randint(0,10000), random.randint(0,10000), random.randint(0,10000)]
        conditional_bool_item= True
        if conditional_bool_item:
            num=random.randint(0,10000)

        context={ "num":num,
        "some_list":some_list
        }
        return context


class AboutView(TemplateView):
    template_name = "about.html"


class ContactView(TemplateView):
    template_name = "contact.html"