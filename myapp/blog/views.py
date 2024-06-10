from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from . import dbConnection
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def createBooks(request):
    if request.method == "POST":
        data = json.loads(request.body)
        dbConnection.dbCollection.insert_one(data)
        response = HttpResponse("Book details are created successfully")
        response.status_code = 201
        return response
    response = HttpResponse("The Request is Invalid")
    response.status_code = 400
    return response

@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def getBooks(request):
    if request.method == "GET":
        data = list(dbConnection.dbCollection.find())

        for item in data:
            item['_id'] = str(item['_id'])

        return JsonResponse(data, safe=False, status=200)
    response = HttpResponse("The Request is Invalid")
    response.status_code = 400
    return response

@csrf_exempt
@api_view(['PUT'])
@permission_classes([AllowAny])
def updateBooks(request, book_id):
    if request.method == "PUT":
        data = json.loads(request.body)
        print(data)
        updated_fields = {key: value for key, value in data.items() if key != "_id"}
        print(type(book_id))
        print(type(" "+book_id))
        dbConnection.dbCollection.update_one({"BookId": " "+book_id}, {"$set": updated_fields})
        response = HttpResponse("Details Updated Successfully")
        response.status_code = 202
        return response
    response = HttpResponse("The Request is Invalid")
    response.status_code = 400
    return response

@csrf_exempt
@api_view(['DELETE'])
@permission_classes([AllowAny])
@permission_classes([AllowAny])
def deleteBooks(request,book_id):
    if request.method == "DELETE":
        dbConnection.dbCollection.delete_one({"BookId":" "+book_id})
        response = HttpResponse("Deleted Successfully")
        response.status_code = 202
        return response
    response = HttpResponse("The Request is Invalid")
    response.status_code = 400
    return response
