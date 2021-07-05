from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=30)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:  # DB와 연동
        managed = True  # 장고가 db를 관리하게 하는것 (defaul = False) 제어의 역전
        db_table = 'posts'

