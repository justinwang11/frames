from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Applicant
from .forms import ApplicantForm1, ApplicantForm2, ApplicantForm3, ApplicantForm4
from django.core.urlresolvers import reverse

# Create your views here.

def wireframe1(request):
    return render(request, 'frames/wireframe1.html')

def wireframe1_new(request):
    if request.method == 'POST':
        form = ApplicantForm1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wireframe2')
        return redirect('wireframe1')
    return redirect('wireframe1')

def wireframe2(request):
    return render(request, 'frames/wireframe2.html')

def wireframe2_new(request):
    if request.method == 'POST':
        instance = Applicant.objects.last()
        form = ApplicantForm2(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('wireframe3')
        return redirect('wireframe1')
    return redirect('wireframe1')

def wireframe3(request):
    return render(request, 'frames/wireframe3.html')

def wireframe3_new(request):
    if request.method == 'POST':
        instance = Applicant.objects.last()
        form = ApplicantForm3(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('wireframe4')
        return redirect('wireframe1')
    return redirect('wireframe1')

def wireframe4(request):
    return render(request, 'frames/wireframe4.html')

def wireframe4_new(request):
    if request.method == 'POST':
        instance = Applicant.objects.last()
        form = ApplicantForm4(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('wireframe5')
        return redirect('wireframe1')
    return redirect('wireframe1')

def wireframe5(request):
    return render(request, 'frames/wireframe5.html')
