from django.urls import path
from accounts import views
from .views import signup_view, verify_otp_view, login_view


urlpatterns = [
    path('',views.index,name='index'),
    path('accounts/signup/',signup_view,name='signup'),
    path('verify_otp/',verify_otp_view,name='verify_otp'),
    path('login/',login_view,name='login'),
]
