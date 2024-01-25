from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('asset.urls')),
    path('docs/', include_docs_urls(title='asset api',public=True))
]
