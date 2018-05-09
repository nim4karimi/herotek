#from django.contrib import admin
from captcha_admin import admin
from markdownx.admin import MarkdownxModelAdmin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog,Author,Entry

admin.site.register(Blog)
admin.site.register(Author)

class EntryPost(SummernoteModelAdmin):
    list_display = ['headline', 'blog',]
    list_filter = ['mod_date']

    summernote_fields = ('body_text',)


admin.site.register(Entry , EntryPost)



# Register your models here.

