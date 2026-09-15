from rest_framework import serializers


class ChatRequestSerializer(serializers.Serializer):

    session_id = serializers.CharField(
        required=True,
        allow_blank=False
    )

    media_type = serializers.ChoiceField(
        choices=[
            ("text/plain", "Plain text"),
            ("application/json", "JSON")
        ],
        default="text/plain"
    )

    content = serializers.JSONField(
        required=True,
        allow_null=False
    )
