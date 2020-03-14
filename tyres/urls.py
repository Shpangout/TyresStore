from django.urls import path

from tyres import views

urlpatterns = [
    path("", views.TyreViews.as_view())

]
