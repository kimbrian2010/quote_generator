from django.contrib import admin
from .models import Book, BookInstance, Genre, Author, Language


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['last_name', 'first_name', ('date_of_birth', 'date_of_death')] #To display fields in the tuple horizontally


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')


# Register your models here.
#admin.site.register(Book)
#admin.site.register(BookInstance)
admin.site.register(Genre)
#admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Language)



