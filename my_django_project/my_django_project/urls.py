from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('face_recognition/', include('face_recognition_app.urls')),
]
