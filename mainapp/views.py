# from django.shortcuts import render
from multiprocessing import context
from tempfile import template
from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
LoginRequiredMixin,
PermissionRequiredMixin,
)
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import (
CreateView,
DeleteView,
DetailView,
ListView,
TemplateView,
UpdateView,
)
from mainapp import models as mainapp_models
from mainapp import forms


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"

    
class NewsListView(ListView):
    template_name = 'mainapp/news_list.html'
    model = mainapp_models.News
    paginate_by = 5
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class NewsCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'mainapp/news_form.html'
    model = mainapp_models.News
    fields = "__all__"

    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.add_news",)


class NewsDetailView(DetailView):
    template_name = 'mainapp/news_detail.html'
    model = mainapp_models.News


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'mainapp/news_form.html'
    model = mainapp_models.News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.change_news",)


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'mainapp/news_confirm_delete.html'
    model = mainapp_models.News
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.delete_news",)


class CourseListView(TemplateView):
    template_name = "mainapp/courses_list.html"

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        context["objects"] = mainapp_models.Courses.objects.all()[:7]
        return context


class CourseDetailView(TemplateView):
    template_name = "mainapp/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(
            mainapp_models.Courses, pk=pk
        )
        context["lessons"] = mainapp_models.Lesson.objects.filter(
            course=context["course_object"]
        )
        context["teachers"] = mainapp_models.CourseTeacher.objects.filter(
            courses=context["course_object"]
        )
        context["feedback_list"] = mainapp_models.CourseFeedback.objects.filter(
            course=context["course_object"]).order_by("-created", "-rating")[:5]
        if not self.request.user.is_anonymous:
            if not mainapp_models.CourseFeedback.objects.filter(
                course=context["course_object"], user=self.request.user).count():
                context["feedback_form"] = forms.CourseFeedbackForm(
                    course=context["course_object"], user=self.request.user)
        
        return context


class CourseFeedbackFormProcessView(LoginRequiredMixin, CreateView):
    model = mainapp_models.CourseFeedback
    form_class = forms.CourseFeedbackForm

    def form_valid(self, form):
        self.object = form.save()
        rendered_card = render_to_string(
            "mainapp/includes/feedback_card.html", context={"item": self.object}
        )
        return JsonResponse({"card": rendered_card})


# class ContactsPageView(TemplateView):
#     template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'


# class CoursesView(TemplateView):
#     template_name = 'mainapp/courses_list.html'


# class DocsView(TemplateView):
#     template_name = 'mainapp/doc_site.html'


# class IndexView(TemplateView):
#     template_name = 'mainapp/index.html'


# class NewsView(TemplateView):
#     template_name = 'mainapp/news.html'

#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         context_data['object_list'] = [
#             {
#                 'title': 'Новость раз',
#                 'preview': 'Прквью для новости раз',
#                 'date': datetime.now()
#             }, {
#                 'title': 'Новость два',
#                 'preview': 'Прквью для новости два',
#                 'date': datetime.now()
#             }, {
#                 'title': 'Новость три',
#                 'preview': 'Прквью для новости три',
#                 'date': datetime.now()
#             }, {
#                 'title': 'Новость четыре',
#                 'preview': 'Прквью для новости четыре',
#                 'date': datetime.now()
#             }, {
#                 'title': 'Новость пять',
#                 'preview': 'Прквью для новости пять',
#                 'date': datetime.now()
#             }, {
#                 'title': 'Новость шесть',
#                 'preview': 'Прквью для новости шесть',
#                 'date': datetime.now()
#             }
#         ]
#         context_data['range'] = range(1, 5)
#         return context_data


# class NewsWithPaginatorView(NewsView):
#     def get_context_data(self, page, **kwargs):
#         context = super().get_context_data(page=page, **kwargs)
#         context["page_num"] = page
#         return context
