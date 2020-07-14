from django.contrib import admin
from Book.models import BookInfo, RoleInfo

# Register your models here.

class RoleIndoAdmin(admin.ModelAdmin):
    """角色model後臺管理介面的管理類別"""
    list_display = ['id', 'rName', 'rGender', 'book']

# 註冊BookInfo
admin.site.register(BookInfo)

# 註冊RoleInfo
admin.site.register(RoleInfo, RoleIndoAdmin)