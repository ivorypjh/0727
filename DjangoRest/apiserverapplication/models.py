from django.db import models

# Create your models here.

# book에 대한 클래스(모델, 테이블) 생성
class Book(models.Model):
    bookid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    store = models.CharField(max_length=50)
    # 날짜에 사용하는 Datefield
    pub_date = models.DateField()