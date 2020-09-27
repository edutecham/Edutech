"""NotesSharingDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='home'),
    path('about/',About,name='about'),
    path('contact/',Contact,name='contact'),
    path('login/',Login,name='login'),
    path('signup/',Signup1,name='signup'),
    path('login_admin/', Login_Admin, name='login_admin'),
    path('profile/', profile, name="profile"),
    path('edit_profile/', Edit_profile, name="edit_profile"),
    path('change_password/', Change_Password, name="change_password"),
    path('logout/', Logout, name="logout"),
    path('logout1/', Logout1, name="logout1"),
    path('upload_notes/', Upload_Notes, name="upload_notes"),
    path('view_mynotes/', View_Mynotes, name="view_mynotes"),
    path('viewallnotesuser/', ViewAllnotesuser, name="viewallnotesuser"),
    path('delete_mynotes/<int:pid>', Delete_Mynotes, name="delete_mynotes"),
    path('admin_home/', Admin_Home, name="admin_home"),
    path('view_users/', View_Users, name="view_users"),
    path('delete_users/<int:pid>', Delete_Users, name="delete_users"),
    path('view_pendingnotes/', view_pendingnotes, name="view_pendingnotes"),
   # path('viewacceptednotes/', viewacceptednotes, name="viewacceptednotes"),
    path('view_allnotes/', view_allnotes, name="view_allnotes"),
    path('view_rejectednotes/', view_rejectednotes, name="view_rejectednotes"),
    path('delete_notes/<int:pid>', Delete_Notes, name="delete_notes"),
    path('edit_status/<int:pid>', Edit_status, name="edit_status"),
    path('forget/', Forget, name="forget"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
