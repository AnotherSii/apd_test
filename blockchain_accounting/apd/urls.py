from django.urls import path, re_path, include

from apd.views import *

app_name = 'apd'
urlpatterns = [
    path('', APD_Test.as_view(), name='test'),
]