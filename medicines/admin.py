# medicines/admin.py

from django.contrib import admin
from .models import Medicine, AlternateMedicine

admin.site.register(Medicine)
admin.site.register(AlternateMedicine)
