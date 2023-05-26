from django.contrib import admin
from .models import sportsCategory, sportsPost
# Register your models here.

class customSportsCategory(admin.ModelAdmin):
    list_display = ('sportsName', 'show_image', 'description', 'urls', 'addDate')
    search_fields = ('sportsName', )

class customSportsPost(admin.ModelAdmin):
    list_display = ('postName', 'show_image', 'urls',)
    search_fields = ('postName', )
    list_filter = ('category', )

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)

admin.site.register(sportsCategory, customSportsCategory)
admin.site.register(sportsPost, customSportsPost)
