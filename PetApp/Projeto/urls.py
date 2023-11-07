from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('Home/', TemplateView.as_view(template_name='html/Home.html'), name='Home'),
]
