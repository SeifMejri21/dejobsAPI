from django.conf.urls import url
from dejobs_api import views

urlpatterns = [
    url(r'^$', views.WelcomeApi),
    url(r'^companies$', views.CompaniesApi),
    url(r'^companies/([0-9]+)$', views.CompaniesApi),
    url(r'^jobs$', views.JobsApi),
    url(r'^jobs/([0-9]+)$', views.JobsApi),
    url(r'^jobs/available/all', views.AllAvailableJobsApi),
    url(r'^jobs/available', views.AvailableJobsApi),
    url(r'^jobs/count', views.AvailableJobsApiCount),
    url(r'^jobs/filters', views.AvailableJobsApiFilters),
]
