

# 登录成功，管理页面
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from project_app.models import Project
from personal.froms import ProjectForm

"""
项目管理
"""
@login_required
def project(request):
    projects = Project.objects.all()
    return render(request,"project.html",{"projects":projects,"type":"list"})

"""
新增
"""
@login_required
def add_project(request):
    if request.method == 'GET':
        return render(request, "project.html", {"type": "add"})
    elif request.method == 'POST':
        name = request.POST.get("name","")
        describe = request.POST.get("describe", "")
        status = request.POST.get("status","")

        if name == "":
            return render(request, "project.html", {"type": "add", "error":"项目名称不能为空"})

        Project.objects.create(name=name,describe=describe,status=status)
        return HttpResponseRedirect("/project/",{"type" : "list"})



"""
修改项目
"""
@login_required
def edit_project(request, pid):
    if request.method == "GET":
        if pid:
            p = Project.objects.get(id=pid)
            form = ProjectForm(instance=p)
            return render(request, "project.html", {"type": "edit",
                                                    "form":form,
                                                    "id":pid})
    elif request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            p = Project.objects.get(id=pid)
            p.name = name
            p.describe = describe
            p.status = status
            p.save()
            return HttpResponseRedirect("/project/", {"type": "list"})

"""
删除项目
"""
@login_required
def del_project(request,pid):
    if request.method == "GET":
        if pid:
            try:
                p = Project.objects.get(id=pid)
            except Project.DoesNotExist:
                return HttpResponseRedirect("/project/", {"type": "list"})
            else:
                p.delete()
    return HttpResponseRedirect("/project/", {"type": "list"})







