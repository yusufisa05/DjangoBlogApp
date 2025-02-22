from django.contrib import admin
from .models import Article,Comment

# Register your models here.

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"] #Admin panelinde verilerin hangi özelliklerinin gözükeceğini belirtiyoruz
    
    list_display_links = ["title","created_date"] #Admin panelinde özelliklere link eklemek için kullanılır

    search_fields = ["title"] #title özelliğine göre admin paneline arama çubuğu ekledik

    list_filter = ["created_date"] #Oluşturulma tarihine göre admin panelinde filtreleme gerçekleştirdik
    class Meta:
        model = Article


