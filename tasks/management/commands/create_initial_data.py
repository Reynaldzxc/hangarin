from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from tasks.models import Priority, Category, Task, Note, Subtask


class Command(BaseCommand):
    help = "Create initial sample data"

    def handle(self, *args, **kwargs):
        fake = Faker()

        high, created = Priority.objects.get_or_create(name="High")
        medium, created = Priority.objects.get_or_create(name="Medium")
        low, created = Priority.objects.get_or_create(name="Low")
        critical, created = Priority.objects.get_or_create(name="Critical")
        optional, created = Priority.objects.get_or_create(name="Optional")

        work, created = Category.objects.get_or_create(name="Work")
        school, created = Category.objects.get_or_create(name="School")
        personal, created = Category.objects.get_or_create(name="Personal")
        finance, created = Category.objects.get_or_create(name="Finance")
        projects, created = Category.objects.get_or_create(name="Projects")
        
        Task.objects.create(
            title=fake.sentence(nb_words=5),
            description=fake.paragraph(),

            deadline=timezone.make_aware(
            fake.date_time_this_month()),
            
            status=fake.random_element(
            elements=["Pending", "In Progress", "Completed"]
            ),
            category=school,
            priority=high
        )

        Task.objects.create(
            title=fake.sentence(nb_words=5),
            description=fake.paragraph(),
  
            deadline=timezone.make_aware(
            fake.date_time_this_month()),
            
            status="In Progress",
            category=projects,
            priority=medium
        )

        Task.objects.create(
            title=fake.sentence(nb_words=5),
            description=fake.paragraph(),

            deadline=timezone.make_aware(
            fake.date_time_this_month()),
           
            status="Completed",
            category=personal,
            priority=low
        )


        Note.objects.create(
        task=Task.objects.first(),
        content=fake.paragraph()
        )

        Subtask.objects.create(
            parent_task=Task.objects.last(),
            title=fake.sentence(nb_words=4),
            status=fake.random_element(
            elements=["Pending", "In Progress", "Completed"])
        )
        
        self.stdout.write(
            self.style.SUCCESS("Initial data created successfully!")
        )