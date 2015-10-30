from django.contrib import admin
#from GetThingsDone.models import UserDetails
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
"""class profile_inline(admin.StackedInline):
    model = UserDetails
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (profile_inline,)"""

#admin.site.unregister(User)
#admin.site.register(User,UserAdmin)
#admin.site.register(UserDetails)
#admin.site.register(Age)
#admin.site.register(Gender)
