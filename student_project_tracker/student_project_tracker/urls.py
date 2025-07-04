
from django.contrib import admin
from django.urls import path
from projectApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',homepage,name='homepage'),
    path('registerpage/',registerpage,name='registerpage'),
    path('loginpage/',loginpage,name='loginpage'),
    path('logoutpage/',logoutpage,name='logoutpage'),

    path('addlist/',addlist,name='addlist'),
    path('projectlist/',projectlist,name='projectlist'),
    path('editpage/<str:id>',editpage,name='editpage'),
    path('deletepage/<str:id>',deletepage,name='deletepage'),
    path('viewpage/<str:id>',viewpage,name='viewpage'),
    path('stategechange/<str:id>',stategechange,name='stategechange'),


]

