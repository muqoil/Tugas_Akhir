from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index,name="index"),
    path('data_pengukuran/', views.data_pengukuran, name="data_pengukuran"),
    path('1/', views.index1,name="index1"),
    path('get_data_sensor/', views.get_data_sensor, name="get_data_sensor"),
    path('daftar_sensor/', views.daftar_sensor, name="daftar sensor"),
    path('data_pengukuran/ajax-posting/', views.ajax_posting, name='ajax_posting'),
]
