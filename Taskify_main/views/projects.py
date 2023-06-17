from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView

from Taskify_main.models import Projects
from Taskify_main.forms import ProjectManageForm
from Taskify.utils import ManageBaseView, get_object_or_none
from Taskify.constants import CREATE_INSTANCE


class ProjectListView(TemplateView):
    template_name = "project_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Projects.objects.all()
        return context


class ProjectManageView(View, ManageBaseView):

    def manage(self, request, *args, **kwargs):
        instance = get_object_or_none(Projects, id=kwargs.get("pk"))
        form = ProjectManageForm(instance=instance, request=request)
        if request.method == "POST":
            form = ProjectManageForm(request.POST, request.FILES, instance=instance, request=request)
            if form.is_valid():
                form.save()
                messages.success(request, CREATE_INSTANCE)
                return redirect("main:project_list")
        return render(request, "project_manage.html", locals())



