from django.contrib import admin
from django.urls import path
from .models import EventInfo
from .views import card_page, form_page
from django.views.generic import TemplateView

urlpatterns = [
    path('', card_page, name='card_page'),
    path('form/', form_page, name='form_page'),
    path('about/', TemplateView.as_view(template_name='stem_app/about.html'), name='about_page'),
]
