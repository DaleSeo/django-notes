from django.contrib import admin
from .models import Note, Tag

class TagInline(admin.TabularInline):
    model = Note.tags.through
    extra = 3

class TagAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ('notes',)
    list_display = ('title', 'description', 'date')
    search_fields = ['title', 'description']

class NoteAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    list_display = ('title', 'hits', 'user')
    list_filter = ['tags', 'date']
    search_fields = ['title', 'content']

admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)
