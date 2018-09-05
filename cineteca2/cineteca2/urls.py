from django.contrib import admin
from django.urls import path,re_path
from peliculas import views
urlpatterns=[
        path('admin/',admin.site.urls),
        path('',views.home,name='home'),
        re_path('peliculas/(\d+)',views.detalles,name='detalles')
        ]
