from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', views.UserListView.as_view()),  # accounts/
    path('<int:pk>/', views.UserDetailView.as_view()),  # accounts/<id>
    path('login/', views.LoginView.as_view()),  # accounts/login/
    path('logout/', views.LogoutView.as_view()),  # accounts/logout/
    path('register/', views.RegistrationView.as_view()),  # accounts/register/
    path('refresh/', TokenRefreshView.as_view()),
    path('forgot/', views.ForgotPasswordView.as_view()),
    path('restore/', views.RestorePasswordView.as_view()),
]
