from django.conf.urls import url
from pyvisualhelper import views

urlpatterns = [
    url('home/', views.HomePageView.as_view()),
    #url('about', views.AboutPageView.as_view()),
    url('about/',views.AboutPageView.as_view()),
    url('renderhtml/',views.renderHtml.as_view())
]