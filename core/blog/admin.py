from django.contrib import admin

from blog.models import Category, Post


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(Category)
