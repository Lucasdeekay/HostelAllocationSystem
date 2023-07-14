from django.urls import path, include
from rest_framework import routers

from Dashboard import views
from Dashboard.api_views import HostelViewSet, RoomViewSet, StudentViewSet
from Dashboard.views import HomeView, LoginView, ForgotPasswordView, ChangePasswordView, RegisterView, LogoutView

app_name = "Dashboard"

router = routers.DefaultRouter()
router.register('hostel', HostelViewSet)
router.register('room', RoomViewSet)
router.register('student', StudentViewSet)

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('register', RegisterView.as_view(), name="register"),
    path('forgot_password', ForgotPasswordView.as_view(), name="forgot_password"),
    path('forgot_password/change_password<int:user_id>', ChangePasswordView.as_view(), name="change_password"),
    path('dashboard', HomeView.as_view(), name="home"),
    path('api', include(router.urls)),
]
