import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import FreelanceProject, Freelancer, Proposal


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['freelanceproject_count'] = FreelanceProject.objects.count()
    ctx['freelanceproject_open'] = FreelanceProject.objects.filter(status='open').count()
    ctx['freelanceproject_in_progress'] = FreelanceProject.objects.filter(status='in_progress').count()
    ctx['freelanceproject_completed'] = FreelanceProject.objects.filter(status='completed').count()
    ctx['freelanceproject_total_budget'] = FreelanceProject.objects.aggregate(t=Sum('budget'))['t'] or 0
    ctx['freelancer_count'] = Freelancer.objects.count()
    ctx['freelancer_available'] = Freelancer.objects.filter(status='available').count()
    ctx['freelancer_busy'] = Freelancer.objects.filter(status='busy').count()
    ctx['freelancer_offline'] = Freelancer.objects.filter(status='offline').count()
    ctx['freelancer_total_hourly_rate'] = Freelancer.objects.aggregate(t=Sum('hourly_rate'))['t'] or 0
    ctx['proposal_count'] = Proposal.objects.count()
    ctx['proposal_submitted'] = Proposal.objects.filter(status='submitted').count()
    ctx['proposal_shortlisted'] = Proposal.objects.filter(status='shortlisted').count()
    ctx['proposal_accepted'] = Proposal.objects.filter(status='accepted').count()
    ctx['proposal_total_bid_amount'] = Proposal.objects.aggregate(t=Sum('bid_amount'))['t'] or 0
    ctx['recent'] = FreelanceProject.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def freelanceproject_list(request):
    qs = FreelanceProject.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'freelanceproject_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def freelanceproject_create(request):
    if request.method == 'POST':
        obj = FreelanceProject()
        obj.title = request.POST.get('title', '')
        obj.client_name = request.POST.get('client_name', '')
        obj.budget = request.POST.get('budget') or 0
        obj.status = request.POST.get('status', '')
        obj.deadline = request.POST.get('deadline') or None
        obj.category = request.POST.get('category', '')
        obj.skills_required = request.POST.get('skills_required', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/freelanceprojects/')
    return render(request, 'freelanceproject_form.html', {'editing': False})


@login_required
def freelanceproject_edit(request, pk):
    obj = get_object_or_404(FreelanceProject, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.client_name = request.POST.get('client_name', '')
        obj.budget = request.POST.get('budget') or 0
        obj.status = request.POST.get('status', '')
        obj.deadline = request.POST.get('deadline') or None
        obj.category = request.POST.get('category', '')
        obj.skills_required = request.POST.get('skills_required', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/freelanceprojects/')
    return render(request, 'freelanceproject_form.html', {'record': obj, 'editing': True})


@login_required
def freelanceproject_delete(request, pk):
    obj = get_object_or_404(FreelanceProject, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/freelanceprojects/')


@login_required
def freelancer_list(request):
    qs = Freelancer.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'freelancer_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def freelancer_create(request):
    if request.method == 'POST':
        obj = Freelancer()
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.skills = request.POST.get('skills', '')
        obj.hourly_rate = request.POST.get('hourly_rate') or 0
        obj.rating = request.POST.get('rating') or 0
        obj.projects_completed = request.POST.get('projects_completed') or 0
        obj.status = request.POST.get('status', '')
        obj.portfolio_url = request.POST.get('portfolio_url', '')
        obj.bio = request.POST.get('bio', '')
        obj.save()
        return redirect('/freelancers/')
    return render(request, 'freelancer_form.html', {'editing': False})


@login_required
def freelancer_edit(request, pk):
    obj = get_object_or_404(Freelancer, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.skills = request.POST.get('skills', '')
        obj.hourly_rate = request.POST.get('hourly_rate') or 0
        obj.rating = request.POST.get('rating') or 0
        obj.projects_completed = request.POST.get('projects_completed') or 0
        obj.status = request.POST.get('status', '')
        obj.portfolio_url = request.POST.get('portfolio_url', '')
        obj.bio = request.POST.get('bio', '')
        obj.save()
        return redirect('/freelancers/')
    return render(request, 'freelancer_form.html', {'record': obj, 'editing': True})


@login_required
def freelancer_delete(request, pk):
    obj = get_object_or_404(Freelancer, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/freelancers/')


@login_required
def proposal_list(request):
    qs = Proposal.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(project_title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'proposal_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def proposal_create(request):
    if request.method == 'POST':
        obj = Proposal()
        obj.project_title = request.POST.get('project_title', '')
        obj.freelancer_name = request.POST.get('freelancer_name', '')
        obj.bid_amount = request.POST.get('bid_amount') or 0
        obj.delivery_days = request.POST.get('delivery_days') or 0
        obj.status = request.POST.get('status', '')
        obj.cover_letter = request.POST.get('cover_letter', '')
        obj.submitted_date = request.POST.get('submitted_date') or None
        obj.save()
        return redirect('/proposals/')
    return render(request, 'proposal_form.html', {'editing': False})


@login_required
def proposal_edit(request, pk):
    obj = get_object_or_404(Proposal, pk=pk)
    if request.method == 'POST':
        obj.project_title = request.POST.get('project_title', '')
        obj.freelancer_name = request.POST.get('freelancer_name', '')
        obj.bid_amount = request.POST.get('bid_amount') or 0
        obj.delivery_days = request.POST.get('delivery_days') or 0
        obj.status = request.POST.get('status', '')
        obj.cover_letter = request.POST.get('cover_letter', '')
        obj.submitted_date = request.POST.get('submitted_date') or None
        obj.save()
        return redirect('/proposals/')
    return render(request, 'proposal_form.html', {'record': obj, 'editing': True})


@login_required
def proposal_delete(request, pk):
    obj = get_object_or_404(Proposal, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/proposals/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['freelanceproject_count'] = FreelanceProject.objects.count()
    data['freelancer_count'] = Freelancer.objects.count()
    data['proposal_count'] = Proposal.objects.count()
    return JsonResponse(data)
