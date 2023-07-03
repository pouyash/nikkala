from django.shortcuts import render

# Create your views here.
from django.views import View


class HomeView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'home/index.html', context)

def nav_component(request):
    context = {

    }
    return render(request, 'utils/nav_component.html', context)

def footer_component(request):
    context = {

    }
    return render(request, 'utils/footer_component.html', context)