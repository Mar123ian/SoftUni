from django.contrib import admin

from note.models import Note, Category


# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...