from rest_framework.parsers import JSONParser

from rest_framework import status
from member.models import MemberVO
from django.http.response import JsonResponse, HttpResponse, Http404
from rest_framework.decorators import api_view, parser_classes
from icecream import ic
from member.serializers import MemberSerializers
import datetime
now = datetime.datetime.now()
# FBV
@api_view(['GET', 'POST'])  #  복수
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
        if serializer.is_valid(): #  데이터 유효성 검사
            serializer.save()  #  데이터를 저장
            return JsonResponse({'result':f'Welcome, {serializer.data.get("name")}'}, status=201)  # jsonresponse는 response를 특정하게 커스터마이징(형식을 주거나 데이터를 시리얼라이즈 ) 해서 전달할수 있게함, 외부로 전달할때
        # alert(`회원가입 완료 : ${res.data.result}`) 여기 있는 res와 JsonResponse가 같다
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])  # 단수
def member(request, pk):
    try:
        print(f'------ {now.strftime("%Y-%m-%d %H:%M:%S")} ------')
        member = MemberVO.objects.filter(username=pk)
        if member is not None:
            ic(member)
        else:
            print('member is None')
    except MemberVO.DoesNotExist:
        return JsonResponse({'result': 'MEMBER-NOT-EXISTS'}, status=201)

    if request.method == 'GET':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'DELETE':
        MemberVO.objects.get(username=pk).delete()
        return JsonResponse({'result': 'Deleted Complete'}, status=201)

@api_view(['POST'])
def login(request):
    try:
        data = request.data['body']
        pk = data['username']
        user_input_password = data['password']
        member = MemberVO.objects.get(pk=pk)  #  멤버 테이블의 값들 중에서 pk(프라이머리키, 인덱스)를
        # member = self.get_object(pk)

        #if(member is not None):    값이 비어있는지 확인

        if user_input_password == member.password:
                serializer = MemberSerializers(member, many=False)
                return JsonResponse(data=serializer.data, safe=False)
        else:
                print("비밀번호가 다릅니다.")
                return JsonResponse({'result':'PASSWORD-FAIL'}, status=201)
    except MemberVO.DoesNotExist:
        return JsonResponse({'result': 'USERNAME-FAIL'}, status=201)
    return HttpResponse(status=104)

@api_view(['PUT']) #  값을 수정하는데 사용
def member_modify(request):
    data = request.data['body']
    update_member = data['member']
    pk = update_member['username']
    member = MemberVO.objects.get(pk=pk)
    serializer = MemberSerializers(member, data=data['member'], partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'result': f'Update Success , {serializer.data.get("name")}'}, status=201)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
