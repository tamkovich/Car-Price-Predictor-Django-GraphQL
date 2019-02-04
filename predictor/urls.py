from django.urls import path

from predictor.views import PredictorView

app_name = 'car'


urlpatterns = [
    path('', PredictorView.as_view(), name='predictor'),
]
