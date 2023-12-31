from pprint import pprint

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from dejobs_api.models import Companies, Jobs
from dejobs_api.repositorty.sql_utils import DbDataLoader
from dejobs_api.serializers import CompanySerializer, JobSerializer
# def restrict_to_specific_ip(view_func):
#     def wrapper(request, *args, **kwargs):
#         allowed_ip = '192.168.1.100'  # Replace with your allowed IP address
#
#         client_ip = request.META.get('REMOTE_ADDR')
#
#         if client_ip != allowed_ip:
#             return HttpResponseForbidden("Access Forbidden")
#
#         return view_func(request, *args, **kwargs)
#
#     return wrapper
from utils.helpers import set_env


# from django.http import HttpResponseForbidden
# from ratelimit.decorators import ratelimit
# decorators.py


@csrf_exempt
def WelcomeApi(request, id=0):
    if request.method == "GET":
        response = {"message": "welcome to DeJobs API", "version": "1.0.0"}
        return JsonResponse(response, safe=False)


# @ratelimit(ip=True, rate='1/s', method=['POST','GET', 'PUT DELETE'], block=True)
# @restrict_to_specific_ip
@csrf_exempt
def CompaniesApi(request, id=0):
    if request.method == "GET":
        companies = Companies.objects.all()
        companies_serializer = CompanySerializer(companies, many=True)
        return JsonResponse(companies_serializer.data, safe=False)

    elif request.method == "POST":
        company_data = JSONParser().parse(request)
        companies_serializer = CompanySerializer(data=company_data)
        if companies_serializer.is_valid():
            companies_serializer.save()
            return JsonResponse("Company Added Successfully", safe=False)
        else:
            print(companies_serializer.errors)
            pprint(company_data)
            print(
                "************************************************************************************************************************")
            print(
                "************************************************************************************************************************")
            return JsonResponse("Failed to Add Company", safe=False)

    # elif request.method == "PUT":
    #     pprint(request)
    #     # company_data = json.loads(request.data)
    #     company_data = JSONParser().parse(request)
    #     company = Companies.objects.get(CompanyId=company_data['company_id'])
    #     companies_serializer = CompanySerializer(company, data=company_data)
    #     if companies_serializer.is_valid():
    #         companies_serializer.save()
    #         return JsonResponse("Company Updated Successfully", safe=False)
    #     else:
    #         return JsonResponse("Failed to Update Company", safe=False)
    #
    # elif request.method == "DELETE":
    #     company = Companies.objects.get(CompanyId=id)
    #     company.delete()
    #     return JsonResponse("Company Deleted Successfully", safe=False)


@csrf_exempt
def JobsApi(request, id=0):
    if request.method == "GET":
        jobs = Jobs.objects.all()
        jobs_serializer = JobSerializer(jobs, many=True)
        return JsonResponse(jobs_serializer.data, safe=False)

    elif request.method == "POST":
        job_data = JSONParser().parse(request)
        jobs_serializer = JobSerializer(data=job_data)
        print(f"jobs_serializer.is_valid: {jobs_serializer.is_valid()}")
        if jobs_serializer.is_valid():
            jobs_serializer.save()
            return JsonResponse("Job Added Successfully", safe=False)
        else:
            print(jobs_serializer.errors)
            pprint(job_data)
            print(
                "**************************************************************************************************************************************************************************************************************************************************************************")
            return JsonResponse("Failed to Add a Job", safe=False)

    elif request.method == "PUT":
        pprint(request)
        job_data = JSONParser().parse(request)
        job = Jobs.objects.get(CompanyId=job_data['job_id'])
        jobs_serializer = JobSerializer(job, data=job_data)
        if jobs_serializer.is_valid():
            jobs_serializer.save()
            return JsonResponse("Job Updated Successfully", safe=False)
        else:
            return JsonResponse("Failed to Update the Job", safe=False)

    # elif request.method == "DELETE":
    #     job = Jobs.objects.get(CompanyId=id)
    #     job.delete()
    #     return JsonResponse("Job Deleted Successfully", safe=False)


@csrf_exempt
def NotParsedCompaniesApi(request, id=0):
    if request.method == "GET":
        ddl = DbDataLoader(db=set_env())
        available_jobs = ddl.get_careers_page_for_not_parsed()
        return JsonResponse(available_jobs, safe=False)


@csrf_exempt
def AvailableJobsApi(request, id=0):
    if request.method == "GET":
        page = int(request.GET.get('page'))
        items = int(request.GET.get('items'))
        ddl = DbDataLoader(db=set_env())
        available_jobs = ddl.get_available_jobs(limit=items, offset=items * (page - 1))
        return JsonResponse(available_jobs, safe=False)


@csrf_exempt
def AllAvailableJobsApi(request, id=0):
    if request.method == "GET":
        ddl = DbDataLoader(db=set_env())
        available_jobs = ddl.get_all_available_jobs()
        return JsonResponse(available_jobs, safe=False)


@csrf_exempt
def AvailableJobsApiCount(request):
    if request.method == "GET":
        ddl = DbDataLoader(db=set_env())
        available_jobs = ddl.get_available_jobs_count()
        return JsonResponse(available_jobs, safe=False)


@csrf_exempt
def AvailableJobsApiFilters(request):
    if request.method == "GET":
        ddl = DbDataLoader(db=set_env())
        jobs_filters = ddl.get_jobs_filters()
        return JsonResponse(jobs_filters, safe=False)
