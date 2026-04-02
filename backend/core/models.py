from django.db import models

class FreelanceProject(models.Model):
    title = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255, blank=True, default="")
    budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("open", "Open"), ("in_progress", "In Progress"), ("completed", "Completed"), ("disputed", "Disputed"), ("cancelled", "Cancelled")], default="open")
    deadline = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=255, blank=True, default="")
    skills_required = models.TextField(blank=True, default="")
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Freelancer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    skills = models.CharField(max_length=255, blank=True, default="")
    hourly_rate = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    rating = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    projects_completed = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("available", "Available"), ("busy", "Busy"), ("offline", "Offline")], default="available")
    portfolio_url = models.URLField(blank=True, default="")
    bio = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Proposal(models.Model):
    project_title = models.CharField(max_length=255)
    freelancer_name = models.CharField(max_length=255, blank=True, default="")
    bid_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    delivery_days = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("submitted", "Submitted"), ("shortlisted", "Shortlisted"), ("accepted", "Accepted"), ("rejected", "Rejected")], default="submitted")
    cover_letter = models.TextField(blank=True, default="")
    submitted_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.project_title
