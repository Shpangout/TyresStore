from django.urls import path

from . import views

urlpatterns = [
    path("", views.TyreView.as_view())

]
