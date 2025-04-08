from django.test import TestCase

class UserTests(TestCase):
    def test_user_endpoint(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

class TeamTests(TestCase):
    def test_team_endpoint(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)

class ActivityTests(TestCase):
    def test_activity_endpoint(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)

class LeaderboardTests(TestCase):
    def test_leaderboard_endpoint(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, 200)

class WorkoutTests(TestCase):
    def test_workout_endpoint(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)
