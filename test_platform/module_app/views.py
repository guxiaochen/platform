"""
模块管理
"""
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from personal.froms import ModuleForm
from module_app.models import Module


@login_required
def module(request):
    modules = Module.objects.all()
    return render(request, "module.html", {"modules": modules, "type": "list"})

@login_required
def add_module(request):
    if request.method == 'GET':
        module_form = ModuleForm()
        return render(request, "module.html", {"type": "add","form":module_form})
    elif request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            project = form.cleaned_data['project']
            status = form.cleaned_data['status']

        if name == "":
            return render(request, "module.html", {"type": "add", "error": "项目名称不能为空"})

        Module.objects.create(project=project,name=name, describe=describe, status=status)
        return HttpResponseRedirect("/module/", {"type": "list"})

@login_required
def edit_module(request,mid):
    if request.method == "GET":
        if mid:
            m = Module.objects.get(id=mid)
            form = ModuleForm(instance=m)
            return render(request, "module.html", {"type": "edit",
                                                    "form":form,
                                                    "id":mid})
    elif request.method == "POST":
        form = ModuleForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            project = form.cleaned_data['project']
            m = Module.objects.get(id=mid)
            m.name = name
            m.describe = describe
            m.status = status
            m.project = project
            m.save()
            return HttpResponseRedirect("/module/", {"type": "list"})

@login_required
def del_module(request,mid):
    if request.method == "GET":
        if mid:
            try:
                m = Module.objects.get(id=mid)
            except Module.DoesNotExist:
                return HttpResponseRedirect("/module/", {"type": "list"})
            else:
                m.delete()
    return HttpResponseRedirect("/module/", {"type": "list"})
