from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Opus)
admin.site.register(Progress)
admin.site.register(UserExp)
admin.site.register(ExpHistory)
admin.site.register(UserPermission)
admin.site.register(Chat)
admin.site.register(UserPermissionBadge)
