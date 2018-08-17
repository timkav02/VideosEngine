from django.contrib import admin
from .models import Video, Flipbook, Tag, Category, Actor

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'channel', 'rating', 'views')
	#list_per_page = 25

class FlipbookAdmin(admin.ModelAdmin):
    list_display = ('video', 'images')
	#list_per_page = 25

class TagAdmin(admin.ModelAdmin):
    list_display = ('video', 'tags')
	#list_per_page = 25

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('video', 'categories')
	#list_per_page = 25

class ActorAdmin(admin.ModelAdmin):
    list_display = ('video', 'actors')
	#list_per_page = 25

admin.site.register(Video, VideoAdmin)
admin.site.register(Flipbook, FlipbookAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Actor, ActorAdmin)