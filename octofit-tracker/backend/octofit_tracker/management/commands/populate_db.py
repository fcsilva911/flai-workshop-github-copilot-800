from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database population...')
        
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        # Create teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Heroes from the Marvel Universe'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Heroes from the DC Universe'
        )
        
        # Create users (superheroes)
        self.stdout.write('Creating users...')
        marvel_heroes = [
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com'},
            {'name': 'Steve Rogers', 'email': 'captain@marvel.com'},
            {'name': 'Thor Odinson', 'email': 'thor@marvel.com'},
            {'name': 'Bruce Banner', 'email': 'hulk@marvel.com'},
            {'name': 'Natasha Romanoff', 'email': 'blackwidow@marvel.com'},
            {'name': 'Peter Parker', 'email': 'spiderman@marvel.com'},
        ]
        
        dc_heroes = [
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com'},
            {'name': 'Clark Kent', 'email': 'superman@dc.com'},
            {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com'},
            {'name': 'Barry Allen', 'email': 'flash@dc.com'},
            {'name': 'Arthur Curry', 'email': 'aquaman@dc.com'},
            {'name': 'Hal Jordan', 'email': 'greenlantern@dc.com'},
        ]
        
        users = []
        for hero in marvel_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                team_id=str(team_marvel._id)
            )
            users.append(user)
            
        for hero in dc_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                team_id=str(team_dc._id)
            )
            users.append(user)
        
        # Create activities
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weight Training', 'Yoga', 'Boxing']
        
        for user in users:
            num_activities = random.randint(5, 15)
            for i in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 120)
                calories = duration * random.randint(5, 12)
                days_ago = random.randint(0, 30)
                activity_date = datetime.now() - timedelta(days=days_ago)
                
                Activity.objects.create(
                    user_id=str(user._id),
                    activity_type=activity_type,
                    duration=duration,
                    calories_burned=calories,
                    date=activity_date,
                    notes=f'{activity_type} session by {user.name}'
                )
        
        # Create leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        for user in users:
            user_activities = Activity.objects.filter(user_id=str(user._id))
            total_calories = sum(activity.calories_burned for activity in user_activities)
            total_activities_count = user_activities.count()
            
            Leaderboard.objects.create(
                user_id=str(user._id),
                total_calories=total_calories,
                total_activities=total_activities_count,
                rank=0  # Will be updated after all entries are created
            )
        
        # Update ranks
        leaderboard_entries = Leaderboard.objects.all().order_by('-total_calories')
        for rank, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()
        
        # Create workouts
        self.stdout.write('Creating workouts...')
        workouts_data = [
            {
                'name': 'Super Soldier Training',
                'description': 'High-intensity training inspired by Captain America',
                'category': 'Strength',
                'difficulty': 'advanced',
                'duration': 60,
                'calories_per_session': 600
            },
            {
                'name': 'Arc Reactor Cardio',
                'description': 'Iron Man inspired cardio workout',
                'category': 'Cardio',
                'difficulty': 'intermediate',
                'duration': 45,
                'calories_per_session': 450
            },
            {
                'name': 'Asgardian Strength',
                'description': 'Thor-style heavy lifting workout',
                'category': 'Strength',
                'difficulty': 'advanced',
                'duration': 75,
                'calories_per_session': 700
            },
            {
                'name': 'Spider Agility',
                'description': 'Spider-Man inspired agility and flexibility training',
                'category': 'Flexibility',
                'difficulty': 'intermediate',
                'duration': 40,
                'calories_per_session': 350
            },
            {
                'name': 'Dark Knight Combat',
                'description': 'Batman-style martial arts and combat training',
                'category': 'Martial Arts',
                'difficulty': 'advanced',
                'duration': 90,
                'calories_per_session': 800
            },
            {
                'name': 'Kryptonian Power',
                'description': 'Superman-level strength and endurance workout',
                'category': 'Strength',
                'difficulty': 'advanced',
                'duration': 60,
                'calories_per_session': 650
            },
            {
                'name': 'Amazonan Warrior',
                'description': 'Wonder Woman inspired warrior training',
                'category': 'Combat',
                'difficulty': 'advanced',
                'duration': 70,
                'calories_per_session': 720
            },
            {
                'name': 'Speed Force Cardio',
                'description': 'Flash-inspired high-speed interval training',
                'category': 'Cardio',
                'difficulty': 'intermediate',
                'duration': 30,
                'calories_per_session': 400
            },
            {
                'name': 'Atlantean Swimming',
                'description': 'Aquaman-style aquatic workout',
                'category': 'Swimming',
                'difficulty': 'beginner',
                'duration': 45,
                'calories_per_session': 380
            },
            {
                'name': 'Willpower Training',
                'description': 'Green Lantern mental and physical conditioning',
                'category': 'Mind-Body',
                'difficulty': 'intermediate',
                'duration': 50,
                'calories_per_session': 420
            },
        ]
        
        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)
        
        # Summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(f'Teams created: {Team.objects.count()}')
        self.stdout.write(f'Users created: {User.objects.count()}')
        self.stdout.write(f'Activities created: {Activity.objects.count()}')
        self.stdout.write(f'Leaderboard entries: {Leaderboard.objects.count()}')
        self.stdout.write(f'Workouts created: {Workout.objects.count()}')
        self.stdout.write(self.style.SUCCESS('Database successfully populated with superhero test data!'))
