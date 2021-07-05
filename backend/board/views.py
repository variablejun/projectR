
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from member.models import MemberVO as Member
from board.serializers import BoardSerializer
from rest_framework.views import APIView
from icecream import ic
from rest_framework.response import Response

class Posts(APIView):
    def post(self, request):

        data = request.data['body']
        ic(request)
        serializer = BoardSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({'result' : f'Welcome, {serializer.data.get("name")}'}, status=201)
        ic(serializer.errors)
        return Response(serializer.errors,status=400)

class Member(APIView):
    def get(self, request):
        pass

@csrf_exempt
def member_list(request):

    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        serializer = BoardSerializer()
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
# Create your views here.
