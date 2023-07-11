from django.shortcuts import render

# Create your views here.
from django.views import View

from about_us.models import AboutUs


class AboutUsView(View):
    def get(self, request):
        about = AboutUs.objects.filter(is_active=True).last()
        context = {
            'about': about
        }
        return render(request, 'about_us/aboutus.html', context)