from django.urls import path
from myproject import views

urlpatterns = [
    path('pdf/', views.pdf, name='pdf'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('address/', views.address, name='address'),
]


