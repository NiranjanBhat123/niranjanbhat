from django.contrib import admin
from .models import *


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'email',)
    search_fields = ('student_id', 'first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'isbn_number', 'title', 'author',)
    search_fields = ('book_id', 'isbn_number', 'title', 'author',)
    list_filter = ('genre',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('id', 'name')


class AdminAdmin(admin.ModelAdmin):
    list_display = ('admin_id', 'first_name', 'last_name', 'email',)
    search_fields = ('admin_id', 'first_name', 'last_name', 'email',)


admin.site.register(Student, StudentAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Admin, AdminAdmin)
