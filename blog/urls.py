from django.contrib import admin
from django.urls import path
from blog_app import views


urlpatterns = [
    path('admin/', admin.site.urls),


    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup'),
    
    
    
    path('show',views.show,name='home'),
    path('addblog',views.add_blog,name='addblog'),
    path('delete<int:id>',views.delete,name='delete'),
    path('update<int:id>',views.update,name='update'),   
    path('contact',views.add_contact,name='contact'),
    path('contacts',views.contact_show,name='contacts'),

]
