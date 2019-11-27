"""multi_client URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from editor import views as editor_views

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^$', editor_views.index, name='index-default'),
    re_path(r'^api/users/$', editor_views.users),
    re_path(r'^api/users/(?P<user_id>[^/]+)/$', editor_views.user),
    re_path(r'^api/documents/(?P<document_id>[^/]+)/$', editor_views.document),
    re_path(r'^api/documents/(?P<document_id>[^/]+)/changes/$', editor_views.document_change, name='document-changes'),
    re_path(r'^(?P<document_id>[^/]+)$', editor_views.index),
]
