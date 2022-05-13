from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User, UserFollowing


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "id",
        "email",
        "username",
        "is_staff",
        "is_active",
    ]
    list_display_links = ["id", "email"]
    list_filter = [
        "email",
        "username",
        "is_staff",
        "is_active",
    ]
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('email',)}),
    )
    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Personal Information"),
            {
                "fields": (
                    "username",
                )
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    search_fields = ["email", "username"]


admin.site.register(User, UserAdmin)

@admin.register(UserFollowing)
class UserFollowingAdmin(admin.ModelAdmin):
    list_display =('id','user_id','following_user_id')