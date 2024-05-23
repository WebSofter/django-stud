from django.urls import path
from blog import views as blog_views
from analysis import views as analysis_views
from dashboard import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),

    #blog
    path('blog/', blog_views.PostViewList, name='blog'),
    path('blog/create', blog_views.PostViewCreation.as_view(), name='blog_create'),
    path('blog/<str:slug>', blog_views.PostViewDetail.as_view(), name='blog_detail'),
    path('blog/<str:slug>/update', blog_views.PostViewUpdation.as_view(), name='blog_update'),

    #analysis
    path('analysis/', analysis_views.AnalysisViewList, name='analysis'),
    path('analysis/create', analysis_views.AnalysisViewCreation.as_view(), name='analysis_create'),
    path('analysis/<int:id>/update', analysis_views.AnalysisViewUpdation.as_view(), name='analysis_update'),

    #
    path('billing/', views.billing, name='billing'),
    path('tables/', views.tables, name='tables'),
    path('vr/', views.vr, name='vr'),
    path('rtl/', views.rtl, name='rtl'),
    path('notification/', views.notification, name='notification'),
    path('profile/', views.profile, name='profile'),

    # Authentication
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name="password_change_done"),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]
