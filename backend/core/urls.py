from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('freelanceprojects/', views.freelanceproject_list, name='freelanceproject_list'),
    path('freelanceprojects/create/', views.freelanceproject_create, name='freelanceproject_create'),
    path('freelanceprojects/<int:pk>/edit/', views.freelanceproject_edit, name='freelanceproject_edit'),
    path('freelanceprojects/<int:pk>/delete/', views.freelanceproject_delete, name='freelanceproject_delete'),
    path('freelancers/', views.freelancer_list, name='freelancer_list'),
    path('freelancers/create/', views.freelancer_create, name='freelancer_create'),
    path('freelancers/<int:pk>/edit/', views.freelancer_edit, name='freelancer_edit'),
    path('freelancers/<int:pk>/delete/', views.freelancer_delete, name='freelancer_delete'),
    path('proposals/', views.proposal_list, name='proposal_list'),
    path('proposals/create/', views.proposal_create, name='proposal_create'),
    path('proposals/<int:pk>/edit/', views.proposal_edit, name='proposal_edit'),
    path('proposals/<int:pk>/delete/', views.proposal_delete, name='proposal_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
