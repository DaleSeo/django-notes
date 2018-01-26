from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'user')
    list_filter = ['date']
    search_fields = ['title', 'memo']

admin.site.register(Note, NoteAdmin)
