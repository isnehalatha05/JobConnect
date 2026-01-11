from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile, Job, Application
from .forms import JobForm, ApplicationForm
from django.contrib.auth.decorators import login_required

def home(request):
    query = request.GET.get('q', '')
    jobs = Job.objects.filter(title__icontains=query) if query else Job.objects.all()
    return render(request, 'home.html', {'jobs': jobs, 'query': query})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, role=role)
        return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.profile.role == 'employer':
                return redirect('employer_dashboard')
            else:
                return redirect('seeker_dashboard')
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def employer_dashboard(request):
    jobs = Job.objects.filter(employer=request.user)
    return render(request, 'employer_dashboard.html', {'jobs': jobs})

@login_required
def seeker_dashboard(request):
    applications = Application.objects.filter(seeker=request.user)
    return render(request, 'seeker_dashboard.html', {'applications': applications})

@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user
            job.save()
            return redirect('employer_dashboard')
    else:
        form = JobForm()
    return render(request, 'post_job.html', {'form': form})

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.seeker = request.user
            app.job = job
            app.save()
            return redirect('seeker_dashboard')
    else:
        form = ApplicationForm()
    return render(request, 'apply_job.html', {'form': form, 'job': job})



