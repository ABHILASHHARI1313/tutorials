from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.list,name="list"),
    path('edit/',views.edit,name="edit"),
    path('create/',views.create,name="create"),

]
