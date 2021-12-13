from django.contrib import admin
from .models import Post

# admin.site.register(Post) 등록법_1

# class PostAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Post, PostAdmin) 등록법_2

@admin.register(Post) # 파이썬의 장식자 문법 Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'is_public' ,'created_at','updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']
    
    #  이런식으로 model말고 admin에서도 구현이 된다.
    def message_length(self, post):
        return f"{len(post.message)} 글자"
    message_length.short_description = '메세지 글자수'