from djongo import models


class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    team_id = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
        
    def __str__(self):
        return self.name


class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'teams'
        
    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.IntegerField()
    date = models.DateTimeField()
    notes = models.TextField(blank=True)
    
    class Meta:
        db_table = 'activities'
        
    def __str__(self):
        return f"{self.activity_type} - {self.duration} mins"


class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.CharField(max_length=255)
    total_calories = models.IntegerField(default=0)
    total_activities = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboard'
        ordering = ['-total_calories']
        
    def __str__(self):
        return f"Rank {self.rank} - User {self.user_id}"


class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=50)  # beginner, intermediate, advanced
    duration = models.IntegerField()  # in minutes
    calories_per_session = models.IntegerField()
    
    class Meta:
        db_table = 'workouts'
        
    def __str__(self):
        return self.name
