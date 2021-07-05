from rest_framework import serializers
from member.models import MemberVO as Member

class MemberSerializers(serializers.Serializer): # vo의 엔티티값들을 직렬화 시키는것

    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = Member
        fields = '__all__'  # vo필드 다 가져오기

    def create(self, validated_data):
        return Member.objects.create(**validated_data)

    def update(self, instance, validated_data):
        Member.objects.filter(pk=instance.username).update(**validated_data)
        return instance

