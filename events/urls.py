from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('reports/', views.reports, name='reports'),
    path('reports/<int:event_id>/', views.reports_detail, name='reports_detail'),
    path('<int:event_id>/', views.detail, name='detail'),
]