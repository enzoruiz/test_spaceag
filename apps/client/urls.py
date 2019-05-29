from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    LogoutView, LoginView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView
)
from .views import HomeView, SignupView

urlpatterns = [
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('', login_required(HomeView.as_view()), name='home'),
    path('signup', SignupView.as_view(), name='signup'),
    path(
        'change-password/', PasswordChangeView.as_view(),
        name='password_change'
    ),
    path(
        'change-password/done', PasswordChangeDoneView.as_view(),
        name='password_change_done'
    ),
    path(
        'reset-password/', PasswordResetView.as_view(),
        name='password_reset'
    ),
    path(
        'reset-password/done', PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'reset-password/<uidb64>/<token>', PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'reset-password/complete', PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]
