"""first_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls import url
import app1


urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^app1/', include(('app1.urls', 'app1'), namespace='app1')),
    # re_path(r'^app1/', include(api_router.urls)),
    # re_path(r'^app1-auth/', include('rest_framework.urls')),
    # url(r'^books/(?P<year>\d{4})/(?P<month>\d{1,2})', views.books)
]
