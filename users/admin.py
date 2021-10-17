from django.contrib import admin
from users.models import User
from products.admin import CartAdminInline

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (CartAdminInline,)

