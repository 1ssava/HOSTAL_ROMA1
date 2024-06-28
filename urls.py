from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('users.urls')),
    path('gestion/', include('hostal.urls')),
    path('uni/', include('universidad.urls'))
]
