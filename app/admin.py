from django.contrib import admin
from app.models import User


# Register your models here.
# admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "mail", "password", "name"]
    list_display_links = ["id", "mail"]


admin.site.register(User, UserAdmin)
