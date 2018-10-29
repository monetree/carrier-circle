from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from finish.views import handler_404,handler_500,handler_400,handler_403
from django.conf.urls import (
                handler400,
                handler403,
                handler404,
                handler500
            )


urlpatterns = [
    path('', include("scrap.urls")),
    path('', include("details.urls")),
    path('', include("finalize.urls")),
    path('', include("finish.urls")),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404 = handler_404
handler500 = handler_500
handler400 = handler_400
handler403 = handler_403
