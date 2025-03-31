
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/rides/', include('ride_booking.urls')),
    path('api/staff/', include('staffs.urls')),

]
