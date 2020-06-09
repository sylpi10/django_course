import time
from django.contrib import admin

from songs.models import Album, Song

admin.site.site_header = 'Amazing admin space'


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('release_date',)
    search_fields = ['name', 'artist_name']

    list_display = ('name', 'artist_name', 'release_date')
    list_editable = ('artist_name',)
    list_filter = ('artist_name',)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    exclude = ('lyrics',)
    autocomplete_fields = ['album']

    list_display = ('name', 'album', 'duration_readable')
    list_editable = ('album',)
    list_filter = ('album__name', 'album__artist_name',)

    def duration_readable(self, obj):
        return time.strftime('%M:%S', time.gmtime(obj.duration))

    duration_readable.short_description = 'Duration'
    duration_readable.admin_order_field = 'duration'


admin.site.register(Album, AlbumAdmin)
# admin.site.register(Song, SongAdmin)
