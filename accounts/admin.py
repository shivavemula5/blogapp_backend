from django.contrib import admin
from accounts.models import UserAccount

class UserAccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserAccount,UserAccountAdmin)