from django.shortcuts import render, redirect, get_object_or_404
from .forms import SiteInformationForm
from .models import SiteInformation, Results
from django.utils.timezone import now
from datetime import datetime


def access_site_information(request):
    if request.method == 'POST':
        form = SiteInformationForm(request.POST)
        if form.is_valid():
            hostname = form.cleaned_data['hostname']
            if Results.objects.filter(site_information__hostname=hostname).exists():
                form.add_error('hostname', 'Hostname already exists')
            else:
                site_info = form.save()
                # Create a Results object with the site information and current timestamp
                Results.objects.create(site_information=site_info, timestamp=now())
                return redirect('results')
    else:
        form = SiteInformationForm()
    return render(request, 'access_site_information.html', {'form': form})

def results(request):
    site_information = SiteInformation.objects.all()
    for site_info in site_information:
        results = Results.objects.filter(site_information=site_info)
        if results.exists():
            site_info.timestamp = results.first().timestamp.strftime('%Y-%m-%d %H:%M:%S')
        else:
            site_info.timestamp = None  # Or any default value you want
    return render(request, 'results.html', {'site_information': site_information})


def clear_results(request):
    SiteInformation.objects.all().delete()
    return redirect('results')

def edit_site_information(request, site_id):
    site_info = get_object_or_404(SiteInformation, pk=site_id)
    if request.method == 'POST':
        form = SiteInformationForm(request.POST, instance=site_info)
        if form.is_valid():
            form.save()
            return redirect('results')
    else:
        form = SiteInformationForm(instance=site_info)
    return render(request, 'edit_site_information.html', {'form': form})