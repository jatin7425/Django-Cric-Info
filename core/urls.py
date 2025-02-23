from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.cricketer_create_view, name='cricketer_create'),
    path('one_player_data/<int:id>/', views.one_player_data, name='one_player_data'),
    path('update-cricketer/<int:id>/', views.update_cricketer, name='update_cricketer'),
    path('del-cricketer/<int:id>/', views.del_cricketer, name='del_cricketer'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('galary/', views.galary, name='galary'),
    path('registration/', views.register, name='registration'),
    path('send_email/', views.send_email, name='send_email'),
    path('loginform/', views.login_view, name='loginform'),
    path('dologout/', views.logout_view, name='dologout'),
    path('', views.home, name='home'),
    path('clear_cache/', views.clear_cache, name='clear_cache'),
]
