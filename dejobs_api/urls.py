from django.conf.urls import url
from dejobs_api import views

urlpatterns = [
    url(r'^companies$', views.CompaniesApi),
    url(r'^companies/([0-9]+)$', views.CompaniesApi),
]
