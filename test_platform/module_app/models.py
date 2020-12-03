from django.db import models
from project_app.models import Project

class Module(models.Model):
    """
    模块表
    """
    # on_delete关联关系，与关联表一块删除
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    name = models.CharField("名称",max_length=50,null=False)
    describe = models.TextField("描述",default="")
    status = models.BooleanField("状态",default=1)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)