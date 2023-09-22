import json
from pprint import pprint

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from dejobs_api.models import Companies, Jobs
from dejobs_api.serializers import CompanySerializer, JobSerializer
from dejobs_api.repositorty.sql_utils import DbDataLoader


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
            return JsonResponse("Failed to Add Company", safe=False)

    elif request.method == "PUT":
        pprint(request)
        # company_data = json.loads(request.data)
        company_data = JSONParser().parse(request)
        pprint(company_data)
        company = Companies.objects.get(CompanyId=company_data['company_id'])
        companies_serializer = CompanySerializer(company, data=company_data)
        if companies_serializer.is_valid():
            companies_serializer.save()
            return JsonResponse("Company Updated Successfully", safe=False)
        else:
            return JsonResponse("Failed to Update Company", safe=False)

    elif request.method == "DELETE":
        company = Companies.objects.get(CompanyId=id)
        company.delete()
        return JsonResponse("Company Deleted Successfully", safe=False)


@csrf_exempt
def JobsApi(request, id=0):
    if request.method == "GET":
        jobs = Jobs.objects.all()
        jobs_serializer = JobSerializer(jobs, many=True)
        return JsonResponse(jobs_serializer.data, safe=False)

    elif request.method == "POST":
        job_data = JSONParser().parse(request)
        jobs_serializer = JobSerializer(data=job_data)
        if jobs_serializer.is_valid():
            jobs_serializer.save()
            return JsonResponse("Job Added Successfully", safe=False)
        else:
            return JsonResponse("Failed to Add aJob", safe=False)

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

    elif request.method == "DELETE":
        job = Jobs.objects.get(CompanyId=id)
        job.delete()
        return JsonResponse("Job Deleted Successfully", safe=False)


@csrf_exempt
def AvailableJobsApi(request, id=0):
    if request.method == "GET":
        ddl = DbDataLoader(db='local')
        available_jobs = ddl.get_available_jobs()
        return JsonResponse(available_jobs, safe=False)
