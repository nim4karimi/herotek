from captcha_admin import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Service , Prod

class ServicePost(SummernoteModelAdmin):
    summernote_fields = ('desc',)


admin.site.register(Service , ServicePost)



class ProdPost(SummernoteModelAdmin):
    summernote_fields = ('desc','body')


admin.site.register(Prod, ProdPost)

