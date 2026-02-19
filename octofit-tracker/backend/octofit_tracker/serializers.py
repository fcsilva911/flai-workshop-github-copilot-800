from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()

    def get__id(self, obj):
        return str(obj._id)

    class Meta:
        model = User
        fields = ['_id', 'email', 'name', 'team_id', 'created_at']


class TeamSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()

    def get__id(self, obj):
        return str(obj._id)

    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'created_at']


class ActivitySerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()

    def get__id(self, obj):
        return str(obj._id)

    class Meta:
        model = Activity
        fields = ['_id', 'user_id', 'activity_type', 'duration', 'calories_burned', 'date', 'notes']


class LeaderboardSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()

    def get__id(self, obj):
        return str(obj._id)

    class Meta:
        model = Leaderboard
        fields = ['_id', 'user_id', 'total_calories', 'total_activities', 'rank', 'updated_at']


class WorkoutSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()

    def get__id(self, obj):
        return str(obj._id)

    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'category', 'difficulty', 'duration', 'calories_per_session']
