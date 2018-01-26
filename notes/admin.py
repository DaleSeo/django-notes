from django.contrib import admin
from .models import Note, Post, PostTag

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'user')
    list_filter = ['date']
    search_fields = ['title', 'memo']

class TagInline(admin.TabularInline):
    model = PostTag
    extra = 3

class PostAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    list_display = ('title', 'date', 'user')
    list_filter = ['date']
    search_fields = ['title', 'memo']

admin.site.register(Note, NoteAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostTag)
