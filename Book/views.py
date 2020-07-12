from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 


# Create your views here.

def testRedirectToBookPage(request):
    """測試：請求到VIEW的邏輯"""
    # return HttpResponse(" >>> 測試 <<< ")
    return HttpResponse("<h1 style='color:red;'> >>> 測試 <<< </h1>")

def testGetBookInfoJson(request):
    """測試：請求到VIEW - JsonResponse"""
    bookData = {
        "bName":'Python之路',
        "bPrice":'399'
    }
    return JsonResponse(bookData)