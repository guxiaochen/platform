from django import forms
from project_app.models import Project
from module_app.models import Module

class ProjectForm(forms.ModelForm):
    # name = forms.CharField(label='名称',max_length=100)
    # describe = forms.CharField(label='描述',widget=forms.Textarea)
    # status = forms.BooleanField(label='状态',required=True)

    class Meta:
        model = Project
        fields = ['name','describe','status']




class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['project','name','describe','status']