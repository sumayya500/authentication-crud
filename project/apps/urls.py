from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_view,name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('home/',views.home_view,name='home'),
    path('logout_view/',views.logout_view,name='logout'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('delete-user/<int:user_id>/',views.delete_user,name='delete_user'),
    path('edit-user/<int:user_id>/',views.edit_user,name='edit_user'),
    path('create-user/',views.create_user,name='create_user'),

]
