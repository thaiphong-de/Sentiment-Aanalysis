from django.contrib import admin

# Register your models here.
from sentiment.models import Review

admin.site.register(Review)