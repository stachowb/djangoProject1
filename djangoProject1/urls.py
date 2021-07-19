from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('driver/', include("apps.drivers.urls")),
    path('company/', include("apps.companies.urls")),
    path('shift/', include('apps.shifts.urls')),
    path('', include("apps.mainpage.urls"))
]
