from django.shortcuts import render    # 返回页面

# Create your views here.
# MTV view
from django.http import HttpResponse,HttpResponseRedirect
"""
认证模块
"""
from django.contrib import auth

# 装饰器？？？，校验登录
from django.contrib.auth.decorators import login_required


# 函数必须有入参，名称可以非request
# 客户端（request）---->服务器（django）请求
# 客户端<-----------response服务器（django）响应
def say_hello(request):

    # get(变量名，变量值->不传参不报错)
    getName = request.GET.get('name',"")
    if getName == "":
        return HttpResponse("请输入name")
    talk = []
    for i in range(3):
        talk.append("hello:"+getName+"\n")
    # return HttpResponse(talk)
    return render(request,"index.html",{"name" : getName})   #跳转页面


"""
登录首页
:param request: 
:return: 
"""
def index(request):

    if request.method == "GET":
        return render(request, "index.html")
    else:
        """
        处理登录请求
        """
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        # print(username+":"+password)
        if username == "" or password == "":
            return render(request, "index.html", {"error": "用户名或密码为空"})

        """
        查询用户是否存在
        """
        user = auth.authenticate(username=username ,password=password)
        print("user--->",user)
        if user is None:
            return render(request, "index.html", {"error": "用户名或密码错误"})
        else:
            auth.login(request,user)  # 记录用户登录的状态，目的防止未登录访问其他路径
            # 重定向跳转页面
            return HttpResponseRedirect("/project/")


def logout(request):
    auth.logout(request)  # 清除缓存并退出
    return HttpResponseRedirect("/index/")





