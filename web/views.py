from django.shortcuts import render, redirect, get_object_or_404

from .services import filter_rest
from .models import *
from .forms import *


def main_view(request):
    rests = Restaurant.objects.all()

    filter_form = SpecChoice(request.GET)
    filter_form.is_valid()
    rests = filter_rest(rests, filter_form.cleaned_data)

    return render(request, 'web/main.html', context={
        'rests': rests,
        'filter_form': filter_form
    })


def specialization_add(request):
    specializations = Specialization.objects.all()
    form = SpecializationForm()
    if request.method == 'POST':
        form = SpecializationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('specializations')
    return render(request, 'web/new_specialization.html', context={
        'spec': specializations,
        'form': form
    })


def rest_add(request):
    form = RestaurantForm()
    if request.method == 'POST':
        form = RestaurantForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('rest_add')
    return render(request, 'web/new_restaurant.html', context={
        'form': form
    })


def rest_edit(request, id=None):
    rest = get_object_or_404(Restaurant, id=id) if id is not None else None
    form = RestaurantForm(instance=rest)
    if request.method == 'POST':
        form = RestaurantForm(data=request.POST, instance=rest)
        if form.is_valid():
            form.save()
            return redirect('main')
    return render(request, 'web/new_restaurant.html', context={
        'form': form
    })


def rest_delete(request, id=None):
    rest = get_object_or_404(Restaurant, id=id)
    rest.delete()
    return redirect('main')


def all_rest_view(request):
    return redirect('main')