from django.db import models


class MemberVO(models.Model):  # 상속

    username = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=12)
    email = models.EmailField()

    class Meta:  # DB와 연동
        managed = True  # 장고가 db를 관리하게 하는것 (defaul = False) 제어의 역전
        db_table = 'members'

    def __str__(self):
        return f'[{self.pk}] {self.username}'