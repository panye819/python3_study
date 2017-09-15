from django.contrib import admin

# Register your models here.
from models import BookInfo
from models import HeroInfo


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 3
    fieldsets = [
        ('base', {'fields': ['btitle']}),
        ('super', {'fields': ['bpub_date']}),
    ]

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)

