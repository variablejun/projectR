from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from member.models import MemberVO
from django.http.response import JsonResponse, HttpResponse, Http404
from rest_framework.decorators import api_view, parser_classes
from icecream import ic
from member.serializers import MemberSerializers
# FBV
@api_view(['GET', 'POST', 'DELETE'])  #  복수
@parser_classes([JSONParser])
def members(request):
    if request.method == 'GET':
        all_members = MemberVO.objects.all()
        serializer = MemberSerializers(all_members, many=True)  #  복수의 값을 받을때 many true 하면 중복값도 뽑아준다
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

@api_view(['GET', 'POST','PUT', 'DELETE'])  # 단수
def member(request):
    if request.method == 'GET':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = request.data['body']
        pk = data['username']
        user_input_password = data['password']
        member = MemberVO.objects.get(pk=pk)  #  멤버 테이블의 값들 중에서 pk(프라이머리키, 인덱스)를
        # member = self.get_object(pk)
        if(member is not None):
            ic(member)
            if user_input_password == member.password:
                serializer = MemberSerializers(member, many=False)
                return JsonResponse(data=serializer.data, safe=False)
            else:
                print("비밀번호가 다릅니다.")
                return JsonResponse({'result':'PASSWORD-FAIL'}, status=201)
        else:
            print("아이디가 없습니다.")
            JsonResponse({'result': "USERNAME-FAIL"},status=201)
        return HttpResponse(status=104)
    elif request.method == 'PUT':
        data = request.data['body']
        update_member = data['member']
        ic(update_member)
        pk = update_member['username']
        member = MemberVO.objects.get(pk=pk)
        user_change_password = update_member['password']
        ic(user_change_password)
        serializer = MemberSerializers(member, data=data['member'], partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result': f'Update Success , {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)