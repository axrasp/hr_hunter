from django.contrib import admin

from .models import HR, Chat


@admin.register(HR)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = (
        'tg_id',
    )
    readonly_fields = [
        'created_at',
        'updated_at'
    ]
    list_display = (
        'tg_id',
        'username',
        'first_name',
        'last_name',
        'updated_at',
        'phone'
    )


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    search_fields = (
        'tg_id',
        'chat'
    )
    readonly_fields = [
        'created_at',
        'updated_at'
    ]
    list_display = (
        'title',
        'chat_id',
        'updated_at',
    )
