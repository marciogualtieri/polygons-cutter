from django.urls import path

from . import views

urlpatterns = [
    path("cutter/", views.PolygonCutterView.as_view(), name="polygon-cutter")
]
