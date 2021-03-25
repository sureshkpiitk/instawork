from rest_framework import serializers

from team.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("id", 'first_name', 'last_name', 'mobile', 'email', 'role')

    # def create(self, validated_data):
    #     pass
    #
    # def update(self, instance, validated_data):
    #     pass
