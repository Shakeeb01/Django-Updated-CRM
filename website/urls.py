from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),    
    path('logout/',views.logout_user,name='logout'),    
    path('register/',views.register_user,name='register'),    
    path('add_record/',views.add_new_record,name='add_record'),    
    path('record/<int:pk>',views.record_detail,name='record'),    
    path('delete-record/<int:pk>',views.delete_record,name='delete_record'),    
    path('update-record/<int:pk>',views.update_record,name='update_record'),    
]