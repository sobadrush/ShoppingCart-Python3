from django.db import models

# Create your models here.

class BoolInfo(models.Model): # 定義BookInfo並繼承 models.Model
    """ 定義書籍Model """

    # define attribute
    bName = models.CharField(max_length=10)

class RoleInfo(models.Model):
    """ 定義角色色Model """

    # define attribute
    rName = models.CharField(max_length=10)
    rGender = models.BooleanField()
    book = models.ForeignKey(BoolInfo, on_delete=models.PROTECT) # [on_delete] ref. https://www.coder.work/article/3185936


# """ 【建立測試TABLE測試連線】ref. https://www.itread01.com/content/1544108421.html """
# class TEST(models.Model):
#     ID = models.IntegerField(primary_key=True,)
#     NAME = models.CharField(max_length=255,)

#     class Meta:	# 如果讀取已有資料的必要引數！
#         db_table = "Test_Table"
        
#     def __str__(self):
#         return self.NAME