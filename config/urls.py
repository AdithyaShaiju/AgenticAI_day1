from django.contrib import admin
from django.http import JsonResponse

from django.urls import (
    path,
    include
)



def api_root(request):
    return JsonResponse(
        {
            "message": "Agent API is running.",
            "chat_endpoint": "/api/chat/",
            "method": "POST"
        }
    )

urlpatterns = [

    path(
        "",
        api_root,
        name="api-root"
    ),

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "api/",
        include(
            "agent_app.urls"
        )
    ),
]
