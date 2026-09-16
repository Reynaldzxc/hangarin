from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from tasks.models import Priority, Category, Task, Note, Subtask


class Command(BaseCommand):
    help = "Create initial sample data"

    def handle(self, *args, **kwargs):
        fake = Faker()

        low, created = Priority.objects.get_or_create(name="Low")
        medium, created = Priority.objects.get_or_create(name="Medium")
        high, created = Priority.objects.get_or_create(name="High")

        school, created = Category.objects.get_or_create(name="School")
        personal, created = Category.objects.get_or_create(name="Personal")
        project, created = Category.objects.get_or_create(name="Project")
        other, created = Category.objects.get_or_create(name="Other")

        Task.objects.create(
            title=fake.sentence(nb_words=5),
            description=fake.paragraph(),
            deadline=timezone.now(),    
            status="Pending",
            category=school,
            priority=high
        )

        Task.objects.create(
            title=fake.sentence(nb_words=5),
            description=fake.paragraph(),
            deadline=timezone.now(),
            status="In Progress",
            category=project,
            priority=medium
        )

        Task.objects.create(
            title=fake.sentence(nb_words=5),
            description=fake.paragraph(),
            deadline=timezone.now(),
            status="Completed",
            category=personal,
            priority=low
        )


        Note.objects.create(
        task=Task.objects.last(),
        content=fake.paragraph()
        )

        Subtask.objects.create(
            parent_task=Task.objects.last(),
            title=fake.sentence(nb_words=4),
            status="Pending"
        )
        
        self.stdout.write(
            self.style.SUCCESS("Initial data created successfully!")
        )