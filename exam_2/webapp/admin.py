from django.contrib import admin
from webapp.models import Poll, Choice

# Register your models here.

class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'question']
    fields = ['question']
    readonly_fields = ['id', 'created_at']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'choice_text']
    fields = ['choice_text', 'poll']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)