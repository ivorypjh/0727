from django.urls import path
from .views import helloAPI, booksapidata, bookapidata

urlpatterns = [
    # /example/hello/ 요청이 오면 helloAPI 함수가 처리
    path("hello/", helloAPI),
    # /example/books 요청이 오면 bookapidata 함수가 처리
    path("books/", booksapidata),
    # bookid 를 받아서 일치하는 1개의 데이터를 찾아오는 것을 bookapidata 함수가 처리
    # url 뒤에 붙어서 작성한 bookid 를 매개변수로 사용
    path("book/<int:bookid>/", bookapidata)
]