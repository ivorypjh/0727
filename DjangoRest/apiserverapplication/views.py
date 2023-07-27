from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Get 요청만 처리
# post 등의 방식도 , 를 통해 추가 가능
@api_view(['get']) # 대소문자 구분하지 않음
def helloAPI(request):
    return Response("REST API!")

from .serializers import Bookserializers
from rest_framework import status
from .models import Book

# 데이터를 삽입하는 POST 요청을 처리
# 데이터를 가져오는데 사용할 Get 방식을 추가
@api_view(['post', 'get'])
def booksapidata(request):
    # 전송 방식을 확인하는 방법은 request.method 를 확인하면 됨.
    if request.method == 'GET':
        # 전체 데이터 가져오기
        books = Book.objects.all()
        serializer = Bookserializers(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    elif request.method == 'POST':
        # 클라이언트가 전송한 데이터를 Model이 사용할 수 있는 데이터로 변환
        bookdata = Bookserializers(data=request.data)
        # print("2") - 이 코드가 실행되지 않으면 Serializable 실패가 문제
        # 유효성 검사
        if bookdata.is_valid():
            # print("3") - 이 코드가 찍히지 않으면 (테이블) 항목 이름이 잘못된 것
            bookdata.save()  # 데이터 저장
            # 성공했을 때 전송한 데이터를 다시 전송
            return Response(bookdata.data, status=status.HTTP_201_CREATED)
        Response(bookdata.errors, status.HTTP_400_BAD_REQUEST)

# 기본키를 가지고 데이터를 1개 찾아오는데 없으면 404 에러를 발생시킴
from rest_framework.generics import get_object_or_404

# bookid 데이터를 받아서 처리하는 함수
# request 외에도 bookid 를 파라미터로 필요로 함
@api_view(['get'])
def bookapidata(request, bookid):
    # 기본키를 가지고 일치하는 데이터 1개를 조회
    # Book.object.get 을 사용하면 데이터가 있는 경우에는 동일함
    # 하지만 일치하는 데이터가 없는 경우 book 은 아무것도 가지지 못하고 에러도 발생하지 않음
    # 여기서는 데이터가 없는 경우 에러로 처리하기 위해 아래처럼 사용
    book = get_object_or_404(Book, bookid = bookid)
    serializer = Bookserializers(book)
    return Response(serializer.data, status=status.HTTP_200_OK)

# ajax 요청을 처리할 ajax 함수
def ajax(request):
    return render(request, "ajax.html")