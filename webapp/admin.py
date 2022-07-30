from django.contrib import admin

# Register your models here.
from webapp.models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_time']
    list_display_links = ['question']
    list_filter = ['question']
    search_fields = ['question']
    fields = ['question', 'created_time', 'updated_time']
    readonly_fields = ['created_time', 'updated_time']


admin.site.register(Choice)
admin.site.register(Poll, PollAdmin)
