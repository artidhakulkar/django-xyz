#here we add urls og or blog app


from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index")


]

