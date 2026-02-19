from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime


class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            name='Test Hero',
            email='testhero@example.com',
            team_id='',
        )

    def test_list_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user(self):
        response = self.client.get(f'/api/users/{self.user._id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Hero')


class TeamAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(
            name='Test Team',
            description='A test team',
        )

    def test_list_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_team(self):
        response = self.client.get(f'/api/teams/{self.team._id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Team')


class ActivityAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.activity = Activity.objects.create(
            user_id='test_user_id',
            activity_type='Running',
            duration=30,
            calories_burned=300,
            date=datetime.now(),
            notes='Test run',
        )

    def test_list_activities(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_activity(self):
        response = self.client.get(f'/api/activities/{self.activity._id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['activity_type'], 'Running')


class LeaderboardAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.entry = Leaderboard.objects.create(
            user_id='test_user_id',
            total_calories=1000,
            total_activities=10,
            rank=1,
        )

    def test_list_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='A test workout',
            category='Strength',
            difficulty='beginner',
            duration=45,
            calories_per_session=400,
        )

    def test_list_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_workout(self):
        response = self.client.get(f'/api/workouts/{self.workout._id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Workout')


class APIRootTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_root(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)

    def test_root_redirects_to_api(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
