
from django.urls import path

from protfolio import views


urlpatterns = [
    path('',views.me),

]
