from django.contrib import admin

# Register your models here.
from .models import GreetingCard, Message
@admin.register(GreetingCard)
class GreetingCardAdmin(admin.ModelAdmin):
    list_display = ('groom_name', 'bride_name', 'slug', 'created_at')
    search_fields = ('groom_name', 'bride_name', 'slug')
    prepopulated_fields = {'slug': ('groom_name', 'bride_name')}
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('card', 'sender_name', 'to', 'created_at')
    search_fields = ('sender_name', 'to')
    list_filter = ('to', 'created_at')
    raw_id_fields = ('card',)