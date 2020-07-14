from django.contrib import admin

from Book.models import BookInfo, RoleInfo

# Register your models here.

# 註冊BookInfo
admin.site.register(BookInfo)

# 註冊RoleInfo
admin.site.register(RoleInfo)