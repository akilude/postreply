from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(PostLikes)
admin.site.register(ReplyLikes)
