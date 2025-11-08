from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User(email='tony@marvel.com', name='Tony Stark', team='Marvel'),
            User(email='steve@marvel.com', name='Steve Rogers', team='Marvel'),
            User(email='bruce@marvel.com', name='Bruce Banner', team='Marvel'),
            User(email='clark@dc.com', name='Clark Kent', team='DC'),
            User(email='diana@dc.com', name='Diana Prince', team='DC'),
            User(email='barry@dc.com', name='Barry Allen', team='DC'),
        ]
        User.objects.bulk_create(users)

        # Activities
        activities = [
            Activity(name='Running', user_email='tony@marvel.com', team='Marvel'),
            Activity(name='Swimming', user_email='steve@marvel.com', team='Marvel'),
            Activity(name='Cycling', user_email='bruce@marvel.com', team='Marvel'),
            Activity(name='Running', user_email='clark@dc.com', team='DC'),
            Activity(name='Swimming', user_email='diana@dc.com', team='DC'),
            Activity(name='Cycling', user_email='barry@dc.com', team='DC'),
        ]
        Activity.objects.bulk_create(activities)

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=300)
        Leaderboard.objects.create(team='DC', points=250)

        # Workouts
        workouts = [
            Workout(name='Push Ups', description='Do 3 sets of 15 reps'),
            Workout(name='Squats', description='Do 3 sets of 20 reps'),
            Workout(name='Plank', description='Hold for 1 minute'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
