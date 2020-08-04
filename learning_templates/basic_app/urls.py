from django.urls import path
from . import views

#FOR RELATIVE TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
