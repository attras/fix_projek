from django.urls import path,include,re_path
# from django.conf.urls import url,handler403

from .views import home

app_name = 'app_setori'

urlpatterns = [
     path('', home.HomeViews.as_view(), name = 'index_home'),
    
]