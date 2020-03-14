from django.shortcuts import render
from django.views.generic.base import View

from .models import Tyre


class TyreView(View):
    def get(self, request):
        tyres = Tyre.objects.all()
        return render(request, "index.html", {"tyre_list": tyres})

