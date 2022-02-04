from django.urls import path, include
from .views import index, signup, signin, logout_user, account, password_change
from django.contrib.auth import views as auth_views
"""the url file is used to associate an url path to a view with path"""

urlpatterns = [
    path('', index, name="user-index"),
    path('signup', signup, name="user-signup"),
    path('signin', signin, name="user-signin"),
    path('logout', logout_user, name="user-logout"),
    path('account', account, name="user-account"),
    path('changepassword', password_change, name="user-change_password"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
    path('login/', auth_views.LoginView.as_view(template_name='users/password_reset_complete.html'), name='login'),
]
