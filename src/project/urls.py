"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),

    path('admin/', admin.site.urls),
    path('meals/' , include('meals.urls' , namespace='meals')),
    path('blog/' , include('blog.urls' , namespace='blog')),
    path('contact/' , include('contact.urls' , namespace='contact')),
    path('about-us/' , include('aboutus.urls' , namespace='aboutus')),
    path('reserve_table/' , include('reservation.urls' , namespace='reservation')),
    path('' , include('home.urls' , namespace='home')),
    
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Resturant AdminPanel"
admin.site.site_title = "Resturant App Admin "
admin.site.site_index_title = "Welcome To Resturant Admin Panel"