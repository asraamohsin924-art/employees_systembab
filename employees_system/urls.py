from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('secret-dashboard-2026/', admin.site.urls),  # 🔥 هذا السطر مهم جداً
    path('', include('employees.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)