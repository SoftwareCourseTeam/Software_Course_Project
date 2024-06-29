"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app01 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/',views.login_me),
    path('login/deal/',views.login_me_deal),
    path('logout/',views.logout),
    path('device_list/',views.device_main),
    path('regist/',views.regist_user),
    path('device/add/',views.device_add),
    path('device/load/',views.device_load),
    path('device/edit/',views.device_edit),
    path('device/edit/new/',views.device_edit_show),
    path('device/delete/',views.device_delete),
    path('device/search/',views.device_search),
    path('device/scrap/',views.device_scrap),
    path('device/scrap/my/',views.device_scrap_my),
    path('device/scrap/submit/',views.device_scrap_submit),
    path('device/search/main/',views.device_search_act),
    path('regist/new/',views.regist_user_new),
    path('device/borrow/',views.device_borrow),
    path('device/borrow/my/',views.device_borrow_my),
    path('device/borrow/submit/',views.device_borrow_submit),
    path('device/borrow/return/',views.device_borrow_return),
    path('device/borrow/delete/',views.device_borrow_delete),
    path('message_center/',views.message_center),
    path('message_center/borrow_requests/',views.message_center_borrow),
    path('message_center/processed_requests/',views.message_center_processed),
    path('message_center/request/',views.message_center_request),
    path('admin_me/',views.admin),
    path('user/info/',views.user_info),
    path('user/edit/',views.user_edit),
    path('profile/load/',views.profile_load),
    path('profile/edit/',views.profile_edit),
    path('profile/change_password/',views.profile_password),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
