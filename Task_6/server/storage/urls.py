from django.urls import path
from . import views

urlpatterns = [
	path('',views.key,name = 'key'),
	path('get_key',views.give_keys, name = 'give_keys'),
]