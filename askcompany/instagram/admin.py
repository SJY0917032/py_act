from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Tag

# admin.site.register(Post) 등록법_1

# class PostAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Post, PostAdmin) 등록법_2

@admin.register(Post) # 파이썬의 장식자 문법 Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public' ,'created_at','updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']
    
    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width:100px;"/>')
        return None
    
    #  이런식으로 model말고 admin에서도 구현이 된다.
    def message_length(self, post):
        return f"{len(post.message)} 글자"
    message_length.short_description = '메세지 글자수'
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass