"""kendo_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mainApp import views
#from kendoui_backend.views import KendoListProviderView

from mainApp.models import Client
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^json$', views.ClientJsonView.as_view(), name='client-json'),
    url(r'^$', views.ClientListView.as_view(), name='client-list'),
    #url(r'^kendo_data$',KendoListProviderView.as_view(model=Client), name='client_kendo')

]
