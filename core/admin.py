from django.contrib import admin

# Register your models here.
from .models import SpamScore, User, GlobalUser

admin.site.register(User)
admin.site.register(GlobalUser)
admin.site.register(SpamScore)
