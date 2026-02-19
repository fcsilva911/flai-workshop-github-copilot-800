from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'team_id', 'created_at')
    search_fields = ('name', 'email')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'user_id', 'duration', 'calories_burned', 'date')
    list_filter = ('activity_type',)
    search_fields = ('user_id', 'activity_type')


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('rank', 'user_id', 'total_calories', 'total_activities', 'updated_at')
    ordering = ('rank',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'difficulty', 'duration', 'calories_per_session')
    list_filter = ('category', 'difficulty')
    search_fields = ('name',)
