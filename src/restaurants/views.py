from django.views.generic import TemplateView
from django.shortcuts import render
from .models import RestaurantLocation

# Create your views here

def restaurants_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    querySet=RestaurantLocation.objects.all()
    context = {
        "object_list" : querySet,
    }
    return render(request, template_name, context)
