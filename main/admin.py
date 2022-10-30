from django.contrib import admin

from main.models import CustomUser, Applications

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Applications)

