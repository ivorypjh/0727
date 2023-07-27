# serializers 와 models.py 파일의 Book을 import
# 동일한 디렉토리에 있는 파일에서 import 하기 때문에 앞에 . 을 사용
from rest_framework import serializers
from .models import Book

class Bookserializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['bookid', 'title', 'author', 'store', 'pub_date']