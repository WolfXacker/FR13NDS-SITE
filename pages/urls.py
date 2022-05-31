from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('my_account', AccountPageView.as_view(), name='my_account'),
]