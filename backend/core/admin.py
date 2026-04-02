from django.contrib import admin
from .models import FreelanceProject, Freelancer, Proposal

@admin.register(FreelanceProject)
class FreelanceProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "client_name", "budget", "status", "deadline", "created_at"]
    list_filter = ["status"]
    search_fields = ["title", "client_name", "category"]

@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "skills", "hourly_rate", "rating", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "email", "skills"]

@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ["project_title", "freelancer_name", "bid_amount", "delivery_days", "status", "created_at"]
    list_filter = ["status"]
    search_fields = ["project_title", "freelancer_name"]
