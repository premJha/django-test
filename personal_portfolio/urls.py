"""personal_portfolio URL Configuration

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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from portfolio.views import home
from blog.views import blogs
from blog.views import blogDetail

app_name = "blog"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('blogs/<int:blogId>', blogDetail,name="blogDetail"),
    path('blogs', blogs),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
