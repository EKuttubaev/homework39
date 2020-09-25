from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def home_page(request):
    return render(request, "home.html", context={
        "header": "Домашняя работа №39"
    })


class HomeView(View):
    def dispatch(self, request, *args, **kwargs):
        return render(request, "home.html", context={
            "header": "Домашняя работа №39"
        })


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        return {
            "header":"About Me page"
        }
class ContactView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        return {
            "header":"Contacts page"
        }