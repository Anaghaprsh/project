# medicines/forms.py

from django import forms

class MedicineSearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Medicine Name')
    components = forms.CharField(widget=forms.Textarea, required=True, label='Components')
    find_alternatives = forms.BooleanField(required=False, label='Find Alternate Medicines', initial=False)
