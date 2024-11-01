from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def func_view_template(request):
    return render(request, "func_template.html")


class ClassViewTemplate(TemplateView):
    template_name = "class_template.html"
