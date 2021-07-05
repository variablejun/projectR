from rest_framework import serializers
from board.models import Post

class BoardSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True) # id 모델에서 자동으로 추가가 되지만 시리얼라이즈는 해주어야한다
    title = serializers.CharField()
    content = serializers.CharField()
    create_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        return instance