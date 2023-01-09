from django.contrib import admin

# Register your models here.

from django.contrib import admin

from music.models import User, Category, Post

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user_id', 'created_date', "category_id")