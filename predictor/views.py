from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse

from logic_application.network import Network


class PredictorView(View):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name)

    def post(self, request, *args, **kwargs):
        network = Network()
        return JsonResponse(network.predict({
            'year_model': request.POST.get('year_model'),
            'mileage': request.POST.get('mileage'),
            'mark': request.POST.get('mark'),
            'fiscal_power': request.POST.get('fiscal_power'),
            'fuel_type': request.POST.get('fuel_type'),
        }))
