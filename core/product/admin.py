# admin.py
from django.contrib import admin
from django.forms import TextInput, Textarea, SelectMultiple, DateInput, CheckboxInput, Select
from django.db import models
from .models import Author, Book, Genre, Publisher
from django.utils.html import format_html


class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    
class PublisherInline(admin.StackedInline):
    model = Publisher
    extra = 0
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'is_alive', 'birth_date', 'photo_display')
    list_filter = ('is_alive', 'birth_date')
    search_fields = ('name', 'bio')
    inlines = [PublisherInline,BookInline]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 60})},
        models.IntegerField: {'widget': TextInput(attrs={'size': '20'})},
        models.BooleanField: {'widget': CheckboxInput()},
        models.DateField: {'widget': DateInput()},
        models.ForeignKey: {'widget': Select(attrs={'style': 'width: auto;'})},
        models.ManyToManyField: {'widget': SelectMultiple(attrs={'style': 'width: auto;'})},
    }
    
    def photo_display(self,obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.photo.url)

    photo_display.short_description = 'Photo'

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'is_bestseller', 'photo_display')
    list_filter = ('pub_date', 'is_bestseller', 'genres')
    search_fields = ('title', 'description')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '40'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
        models.IntegerField: {'widget': TextInput(attrs={'size': '10'})},
        models.BooleanField: {'widget': CheckboxInput()},
        models.DateField: {'widget': DateInput()},
        models.ForeignKey: {'widget': Select(attrs={'style': 'width: auto;'})},
        models.ManyToManyField: {'widget': SelectMultiple(attrs={'style': 'width: auto;'})},

    }
    def photo_display(self,obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.cover_image.url)

    photo_display.short_description = 'Photo'

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name',)
    search_fields = ('name',)
    

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Publisher)