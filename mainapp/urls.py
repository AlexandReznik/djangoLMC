from mainapp import views
from django.urls import path
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('contacts/', views.ContactsView.as_view()),
    path('courses/', views.CoursesView.as_view()),
    path('docs/', views.DocsView.as_view()),
    path('mainapp/', views.IndexView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('news/', views.NewsView.as_view()),
]