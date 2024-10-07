from django.contrib import admin

from .models import DjangoClasses


admin.site.register(DjangoClasses)

# Import the class model to the admin panel.