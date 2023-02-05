from django.contrib import admin
from .models import User, Subscription, Status, EventHistory
# Register your models here.

admin.site.register(User)
admin.site.register(Subscription)
admin.site.register(Status)
admin.site.register(EventHistory)