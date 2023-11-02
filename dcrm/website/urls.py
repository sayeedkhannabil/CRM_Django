from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('record/', views.record, name='showRecord'),
    path('case/', views.case, name='showCase'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('case/<int:pk>', views.customer_case, name='case'),
    path('delete_case/<int:pk>', views.delete_case, name='delete_case'),
    path('add_case/', views.add_case, name='add_case'),
    path('update_case/<int:pk>', views.update_case, name='update_case'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

