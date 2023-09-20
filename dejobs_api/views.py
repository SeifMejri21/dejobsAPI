from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from dejobs_api.models import Companies, Jobs
from dejobs_api.serializers import CompanySerializer, JobSerializer


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
            return JsonResponse("Added Successfully", safe=False)
        else:
            return JsonResponse("Failed to Add", safe=False)

    elif request.method == "PUT":
        company_data = JSONParser().parse(request)
        company = Companies.objects.get(CompanyId=company_data['company_id'])
        companies_serializer = CompanySerializer(company, data=company_data)
        if companies_serializer.is_valid():
            companies_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        else:
            return JsonResponse("Failed to Update", safe=False)

    elif request.method == "DELETE":
        company = Companies.objects.get(CompanyId=id)
        company.delete()
        return JsonResponse("Deleted Successfully", safe=False)
