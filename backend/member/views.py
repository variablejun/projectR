from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from member.models import MemberVO

from rest_framework.decorators import api_view, parser_classes
from icecream import ic
from member.serializers import MemberSerializers
# FBV
@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([JSONParser])
def members(request):
    if request.method == 'GET':
        all_members = MemberVO.objects.all()
        serializer = MemberSerializers(all_members, many=True)
        return JsonResponse(data=serializer.data, safe=False)  #  여기에 들어간다. return이 있는 함수 export const memberList = () => axios.get(`${SERVER}adm/member/list`)
    elif request.method == 'POST':
        new_member = request.data['body']  # body에 있는 데이터를 뽑아 저장해준다.
        ic(new_member)
        serializer = MemberSerializers(data = new_member)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result':f'Welcome, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def member(request, pk):
    if request.method == 'GET':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)