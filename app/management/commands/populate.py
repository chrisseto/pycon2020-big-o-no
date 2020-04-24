import random
from django.db import transaction
from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from app.models import *

class Command(BaseCommand):
    help = 'Populate the database will fake data'

    def handle(self, *args, **options):
        fake = Faker()

        # Generate fake data and hold it in memory.
        # Selecting random entries from these lists will be faster than 
        # generating a new entry every time
        words = [fake.word() for _ in range(75)]
        names = [fake.name() for _ in range(100)]
        emails = [fake.email() for _ in range(100)]
        sentences = [fake.sentence() for _ in range(75)]
        paragraphs = [fake.paragraph() for _ in range(50)]

        with transaction.atomic():
            tags = Tag.objects.bulk_create([
                Tag(text=word) for word in words
            ])

            users = User.objects.bulk_create([
                User(name=random.choice(names))
                for _ in range(500)
            ])

            Email.objects.bulk_create([
                Email(email=random.choice(emails), user=user)
                for user in users
                for _ in range(random.randint(1, 10))
            ])

            projects = Project.objects.bulk_create([
                Project(title=random.choice(sentences), body=random.choice(paragraphs))
                for _ in range(1000)
            ])

            Project.tags.through.objects.bulk_create([
                Project.tags.through(project=project, tag=tag)
                for project in projects
                for tag in random.sample(tags, random.randint(0, 50))
            ])

            Contributor.objects.bulk_create([
                Contributor(project=project, user=user)
                for project in projects
                for user in random.sample(users, random.randint(1, 250))
            ])
