# from django.shortcuts import render
from tempfile import template
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'
    
class CoursesView(TemplateView):
    template_name = 'mainapp/courses_list.html'
    
class DocsView(TemplateView):
    template_name = 'mainapp/doc_site.html'

class IndexView(TemplateView):
    template_name = 'mainapp/index.html'
    
class LoginView(TemplateView):
    template_name = 'mainapp/login.html'
    
class NewsView(TemplateView):
    template_name = 'mainapp/news.html'
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = [
            {
                'title': 'Новость раз',
                'preview': 'Прквью для новости раз',
                'date': '2022-01-01'
            },{
                'title': 'Новость два',
                'preview': 'Прквью для новости два',
                'date': '2022-01-01'
            },{
                'title': 'Новость три',
                'preview': 'Прквью для новости три',
                'date': '2022-01-01'
            },{
                'title': 'Новость четыре',
                'preview': 'Прквью для новости четыре',
                'date': '2022-01-01'
            },{
                'title': 'Новость пять',
                'preview': 'Прквью для новости пять',
                'date': '2022-01-01'
            },{
                'title': 'Новость шесть',
                'preview': 'Прквью для новости шесть',
                'date': '2022-01-01'
            }
        ]
        return context_data