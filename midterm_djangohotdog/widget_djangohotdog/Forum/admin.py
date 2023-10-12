from django.contrib import admin
from .models import ForumPost, Reply
from dashboard.models import WidgetUser

class ForumPostAdmin(admin.ModelAdmin):
    model = ForumPost
    list_display = ('title', 'author', 'body', 'pub_datetime',)

class ReplyAdmin(admin.ModelAdmin):
    model = Reply
    list_display = ('author', 'body', 'pub_datetime','forum_post')


admin.site.register(ForumPost, ForumPostAdmin)
admin.site.register(Reply, ReplyAdmin)
