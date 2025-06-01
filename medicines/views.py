import random
from django.shortcuts import render
from .forms import MedicineSearchForm
from .models import Medicine
import json

# Function to generate random chart data
def generate_random_chart_data():
    # List of random medicine names
    medicines = [f"Medicine {i+1}" for i in range(5)]
    # List of random prices (for example between 5 and 50)
    prices = [round(random.uniform(5, 50), 2) for _ in range(5)]
    
    # Prepare chart data for rendering
    chart_data = {
        'labels': medicines,
        'data': prices,
    }
    
    return chart_data

def search(request):
    if request.method == 'POST':
        form = MedicineSearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            components = form.cleaned_data['components']
            medicines = Medicine.objects.filter(components__icontains=components)
            alternatives = []

            for medicine in medicines:
                alternatives += list(medicine.alternatives.all())

            # Prepare random chart data
            chart_data = generate_random_chart_data()

            return render(request, 'medicines/results.html', {
                'medicines': medicines,
                'alternatives': alternatives,
                'name': name,
                'chart_data': chart_data,  # Pass chart data here
            })
    else:
        form = MedicineSearchForm()
    return render(request, 'medicines/home.html', {'form': form})

def home(request):
    form = MedicineSearchForm()
    return render(request, 'medicines/home.html', {'form': form})
