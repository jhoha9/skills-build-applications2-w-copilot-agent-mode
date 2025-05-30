from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.name, "Test User")

class TeamModelTest(TestCase):
    def test_team_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        team = Team.objects.create(name="Test Team")
        team.members.add(user)
        self.assertEqual(team.name, "Test Team")
        self.assertIn(user, team.members.all())

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        activity = Activity.objects.create(user=user, activity_type="Running", duration=30, date="2025-05-30")
        self.assertEqual(activity.activity_type, "Running")
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Test Workout", description="Test Description")
        self.assertEqual(workout.name, "Test Workout")
