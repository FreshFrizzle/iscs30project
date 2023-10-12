from django.contrib import admin
from .models import Announcement, Reaction

class AnnouncementAdmin(admin.ModelAdmin):
    model = Announcement
    list_display = ('title', 'author', 'body', 'pub_datetime',)

class ReactionAdmin(admin.ModelAdmin):
    model = Reaction
    list_display = ('announcement', 'name', 'tally',)

admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Reaction, ReactionAdmin)
