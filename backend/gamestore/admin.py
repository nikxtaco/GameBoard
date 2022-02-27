from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Hero, Platform, Publisher, Game, Character

admin.site.register(Hero)
admin.site.register(Platform)
admin.site.register(Publisher)
admin.site.register(Game)
admin.site.register(Character)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Account Details', {'fields': ('username', 'first_name', 'last_name', 'country', 'follows')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active',)}
        ),
        ('Account Details', {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'country', 'follows',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)