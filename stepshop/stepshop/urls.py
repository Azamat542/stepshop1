from django.contrib import admin
from django.urls import path, include

from stepshop.views import index, contacts, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('contacts/', contacts),
    path('about/', about),
    path('products/', include('products.urls')),
]
