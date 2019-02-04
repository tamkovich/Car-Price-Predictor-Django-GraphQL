from django.urls import path

from predictor.views import predictor

urlpatterns = [
    path('', predictor, name='predictor'),
]
