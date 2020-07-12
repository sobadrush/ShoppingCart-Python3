from django.contrib import admin
from django.urls import path
from Book.views import testRedirectToBookPage, testGetBookInfoJson

urlpatterns = [
    # path("getAllBooks", "View函數")
    path("getAllBooks", testRedirectToBookPage), # 網址列敲: http://127.0.0.1:8000/book/getAllBooks 會轉到 testRedirectToBookPage 函數
    path("getAllBooksJson", testGetBookInfoJson) # 網址列敲: http://127.0.0.1:8000/book/getAllBooksJson 會轉到 testGetBookInfoJson 函數
]