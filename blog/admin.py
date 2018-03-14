#from django.contrib import admin
from captcha_admin import admin

from markdownx.admin import MarkdownxModelAdmin
from .models import Blog,Author,Entry

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry , MarkdownxModelAdmin)

# Register your models here.

