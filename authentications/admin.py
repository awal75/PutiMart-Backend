from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUsers


@admin.register(CustomUsers)
class CustomUserAdmin(UserAdmin):
    model = CustomUsers

    # List page
    list_display = ('email','first_name','last_name','date_joined', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    readonly_fields = ('date_joined',) 

    # Detail/Edit page
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Add user page
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',  'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

    search_fields = ('email',)
    ordering = ('-date_joined',)

    # Because we removed username field
    filter_horizontal = ('groups', 'user_permissions')