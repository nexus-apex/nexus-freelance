from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import FreelanceProject, Freelancer, Proposal
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusFreelance with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusfreelance.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if FreelanceProject.objects.count() == 0:
            for i in range(10):
                FreelanceProject.objects.create(
                    title=f"Sample FreelanceProject {i+1}",
                    client_name=f"Sample FreelanceProject {i+1}",
                    budget=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["open", "in_progress", "completed", "disputed", "cancelled"]),
                    deadline=date.today() - timedelta(days=random.randint(0, 90)),
                    category=f"Sample {i+1}",
                    skills_required=f"Sample skills required for record {i+1}",
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 FreelanceProject records created'))

        if Freelancer.objects.count() == 0:
            for i in range(10):
                Freelancer.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    email=f"demo{i+1}@example.com",
                    skills=f"Sample {i+1}",
                    hourly_rate=round(random.uniform(1000, 50000), 2),
                    rating=round(random.uniform(1000, 50000), 2),
                    projects_completed=random.randint(1, 100),
                    status=random.choice(["available", "busy", "offline"]),
                    portfolio_url=f"https://example.com/{i+1}",
                    bio=f"Sample bio for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Freelancer records created'))

        if Proposal.objects.count() == 0:
            for i in range(10):
                Proposal.objects.create(
                    project_title=f"Sample Proposal {i+1}",
                    freelancer_name=f"Sample Proposal {i+1}",
                    bid_amount=round(random.uniform(1000, 50000), 2),
                    delivery_days=random.randint(1, 100),
                    status=random.choice(["submitted", "shortlisted", "accepted", "rejected"]),
                    cover_letter=f"Sample cover letter for record {i+1}",
                    submitted_date=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 Proposal records created'))
