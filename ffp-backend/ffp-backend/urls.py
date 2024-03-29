"""ffp-backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path, re_path
from FPA_FOD_PLUS import views
from django.conf import settings

urlpatterns = [
    path(settings.DJANGO_API_ROUTE, include([
        path('admin/', admin.site.urls),
        # re_path(r'^heatmap/$', views.heat_map),
        re_path(r'^search/$', views.perform_search),
        re_path(r'^fire/$', views.fire_by_id),
        re_path(r'^variable_list/$', views.variable_list),
        re_path(r'^distinct_years_list/$', views.distinct_years_list),
        re_path(r'^distinct_states_list/$', views.distinct_states_list),
        re_path(r'^distinct_counties_list', views.distinct_counties_list),
        re_path(r'^geojson_list', views.geojson_list),
        re_path(r'^subset_csv', views.subset_csv),
#        re_path(r'^field_list', views.distinct_field_list),
    ]
    ))
]
