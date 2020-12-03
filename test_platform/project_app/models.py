from django.db import models

# Create your models here.
# M：Model      ---model
# T：Templeate   --view
# V：View   ---Controller
# Model（模型）表示应用程序核心（比如数据库列表）
# View(视图) 显示数据（数据库记录）
# Controller（控制器）处理输入（写入数据库记录）

"""
1、pymysql，需要写sql语句

2、orm像操作对象一样的操作数据库
python ---> pymysql -->mysql
django --->  orm --> pymysql驱动 --> mysql

"""
from django.db import models
class Project(models.Model):
    name = models.CharField("名称",max_length=50,null=False)
    describe = models.TextField("描述",default="")
    status = models.BooleanField("状态",default=1)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    # 解决下拉数据为object的情况
    def __str__(self):
        return self.name



