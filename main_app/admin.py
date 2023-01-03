from django.contrib import admin
from .models import News, Post, answer, question, about
# Register your models here.
admin.site.register(News)
admin.site.register(answer)
admin.site.register(question)
admin.site.register(Post)
admin.site.register(about)
