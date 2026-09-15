import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .agent import run_agent
from .serializers import ChatRequestSerializer


class ChatView(APIView):

    def get(self, request):
        return Response(
            {
                "message": "Chat API is running.",
                "method": "POST",
                "endpoint": "/api/chat/",
                "request_body": {
                    "session_id": "demo",
                    "media_type": "text/plain",
                    "content": "Hello"
                }
            }
        )

    def post(self, request):

        request_data = request.data.copy()

        if "content" not in request_data and "message" in request_data:
            request_data["content"] = request_data["message"]

        serializer = ChatRequestSerializer(
            data=request_data
        )

        serializer.is_valid(raise_exception=True)

        session_id = serializer.validated_data["session_id"]
        media_type = serializer.validated_data["media_type"]
        content = serializer.validated_data["content"]

        if media_type == "application/json" and not isinstance(content, str):
            content = json.dumps(content)

        if not isinstance(content, str):
            content = str(content)

        try:

            result = run_agent(
                session_id=session_id,
                user_message=content
            )

            return Response(
                {
                    "session_id": session_id,
                    "media_type": media_type,
                    "content": result["answer"],
                    **result
                }
            )

        except Exception as exc:

            return Response(
                {
                    "error": str(exc)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )