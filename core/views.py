from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site

def home_view(request):
    current_site = str(get_current_site(request)).split(":")[0]
    print(current_site)
    return HttpResponse("hello")
