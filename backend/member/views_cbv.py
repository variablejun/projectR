from django.shortcuts import render
from django.urls import path
from . import views_cbv
# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from member.models import MemberVO as Member
from member.serializers import MemberSerializers
from rest_framework.views import APIView
from icecream import ic
from rest_framework.response import Response
from django.contrib.auth.models import User

class Members(APIView):
    def post(self, request):

        data = request.data['body']
        ic(request)
        serializer = MemberSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({'result' : f'Welcome, {serializer.data.get("name")}'}, status=201)
        ic(serializer.errors)
        return Response(serializer.errors,status=400)

class Member(APIView):

    def get(self, request, format = None):
        data = request.data['body']
        pk = data['username']
        user_input_password = data['password']
        member = self.get_object(pk)
        if user_input_password == member.password:
            return Response({'result': 'succese'}, status=201)
        return HttpResponse(status=104)

@csrf_exempt
def member_list(request):

    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        serializer = MemberSerializers()
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MemberSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)