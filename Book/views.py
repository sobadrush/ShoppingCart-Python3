from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 


# Create your views here.

def toIndexPage(request):
    """測試：請求到VIEW的邏輯"""
    # return HttpResponse(" >>> 測試 <<< ")

    empList = [] 
    empList.append({ "empName" : "Roger", "empAge" : "30" })
    empList.append({ "empName" : "Kelly", "empAge" : "26" })
    empList.append({ "empName" : "Cater", "empAge" : "28" })

    # 上下文是一個dict
    context = {
        "empList" : empList
    }

    # 呼叫template
    return render(request, "index.html", context) # template的路徑 ( 要先在settings.py中告訴Django自訂的template在哪, 設定 TEMPLATES.DIR )


def testRedirectToBookPage(request):
    """測試：請求到VIEW的邏輯"""
    # return HttpResponse(" >>> 測試 <<< ")
    return HttpResponse("<h1 style='color:red;'> @@@ 測試 @@@ </h1>")

def testGetBookInfoJson(request):
    """測試：請求到VIEW - JsonResponse"""
    bookData = {
        "bName":'Python之路',
        "bPrice":'399'
    }
    return JsonResponse(bookData)