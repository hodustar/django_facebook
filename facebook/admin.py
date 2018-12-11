from django.contrib import admin

#Register your model here.
from facebook.models import Article
from facebook.models import Page
from facebook.models import Comment

admin.site.register(Article)
admin.site.register(Page)
admin.site.register(Comment)