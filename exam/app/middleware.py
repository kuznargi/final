from django.http import HttpResponseRedirect
from django.urls import reverse

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            response = self.get_response(request)
        else:
            return HttpResponseRedirect(reverse('home'))
        return response
