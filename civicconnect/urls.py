from django.urls import path
from . import views

urlpatterns = [
    path('analytics/', views.analytics_dashboard, name='analytics_dashboard'),
    path('', views.root_redirect, name='root'),
    path('login/', views.login_page, name='login'),
    path('auth/verify', views.verify_token, name='verify_token'),
    path('register/', views.register_page, name='register_page'),
    path('auth/create_user', views.auth_create_user, name='auth_create_user'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # APIs
    path('api/reports/', views.get_reports, name='get_reports'),
    path('api/users/create', views.api_create_user, name='api_create_user'),
    path('api/reports/create', views.api_create_report, name='api_create_report'),
    path('api/users/increment', views.api_increment_report_count, name='api_increment_report_count'),
    path('api/reports/generate_fixes', views.api_generate_fix_suggestions, name='api_generate_fix_suggestions'),
    path('api/analytics/overview/', views.api_analytics_overview, name='api_analytics_overview'),
    path('api/analytics/trends/', views.api_analytics_trends, name='api_analytics_trends'),
    path('api/analytics/departments/', views.api_analytics_departments, name='api_analytics_departments'),
    path('api/analytics/response-times/', views.api_analytics_response_times, name='api_analytics_response_times'),
    path('api/analytics/geographic/', views.api_analytics_geographic, name='api_analytics_geographic'),
]
