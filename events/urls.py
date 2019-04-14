from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:event_id>/', views.detail, name='detail'),
    # path('/add', views.add_event, name='add_event'), # no id...
    path('reports/', views.reports, name='reports'),
    path('reports/<int:event_id>/', views.reports_detail, name='reports_detail'),
    path('sponsorships/', views.sponsorships, name='sponsorships'),
    path('sponsorships/<int:event_id>/', views.sponsorships_detail, name='sponsorships_detail'),
]

urlpatterns += [  
    path('create/', views.EventCreate.as_view(), name='event_create'),
    path('<int:pk>/update/', views.EventUpdate.as_view(), name='event_update'),
    path('<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),
]

urlpatterns += [  
    path('reports/create/', views.ReportCreate.as_view(), name='report_create'),
    path('reports/<int:pk>/update/', views.ReportUpdate.as_view(), name='report_update'),
    path('reports/<int:pk>/delete/', views.ReportDelete.as_view(), name='report_delete'),
]

urlpatterns += [  
    path('sponsorships/create/', views.SponsorshipCreate.as_view(), name='sponsorship_create'),
    path('sponsorships/<int:pk>/update/', views.SponsorshipUpdate.as_view(), name='sponsorship_update'),
    path('sponsorships/<int:pk>/delete/', views.SponsorshipDelete.as_view(), name='sponsorship_delete'),
]