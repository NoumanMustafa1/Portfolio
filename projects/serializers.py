from rest_framework import serializers
from projects.models import ProjectInfo


class ProjectInfo_Serializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectInfo
        fields = [
            "github_url",
            "live_url",
            "project_name",
            "project_description",
            "project_image",
            "project_id",
            "project_id",
            "show",
        ]
