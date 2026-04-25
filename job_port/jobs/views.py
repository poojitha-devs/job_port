from django.shortcuts import render, redirect,get_object_or_404
from .models import Job
from .forms import ApplicationForm

def home(request):
    return render(request,'home.html')
def jobs(request):
    return render(request,'jobs.html')
def login(request):
    return render(request,'login.html')
def registration(request):
    return render(request,'registration.html')
def job_list(request):
    jobs = Job.objects.all().order_by('-posted_on')
    return render(request,'job_list.html',{'jobs':jobs})
def job_details(request,job_id):
    job = get_object_or_404(Job,pk=job_id)
    form = ApplicationForm()
    return render(request,'job_details.html',{'job':job,'form':form})
def job_apply(request,job_id):
    if request.method == 'POST':
        job = Job.objects.get(pk=job_id)
        form = ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            return redirect('job_details',job_id=job_id)
        else:
            return render(request,'job_details.html',{'form':form,'job':job})
    return redirect('jobs')

