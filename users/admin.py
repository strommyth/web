from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

from import_export.admin import ImportExportModelAdmin


class UserAdminConfig(UserAdmin,ImportExportModelAdmin):
    model = NewUser
    search_fields = ('email', 'user_name',)
    list_filter = ('is_active', 'is_staff','is_state',)
    list_display = ('id_numbers','email', 'user_name',
                    'is_active', 'is_staff','is_state')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'id_numbers','password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id_numbers', 'email', 'user_name', 'password1', 'password2', 'is_active', 'is_staff','is_state')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)