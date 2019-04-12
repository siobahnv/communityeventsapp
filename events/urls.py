from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:event_id>/', views.detail, name='detail'),
    path('reports/', views.reports, name='reports'),
    path('reports/<int:event_id>/', views.reports_detail, name='reports_detail'),
    path('sponsorships/', views.sponsorships, name='sponsorships'),
    path('sponsorships/<int:event_id>/', views.sponsorships_detail, name='sponsorships_detail'),
]