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
        print(request.POST)
        return JsonResponse({'price': '100500'})
