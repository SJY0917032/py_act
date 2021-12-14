from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y%m%d')
    tag_set = models.ManyToManyField('Tag', blank=True) # 태그가 없을수도 있기에 blank를 넣어줘야한다.
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString과 유사
    def __str__(self):
        # return f"custom Post Obejct ({self.id})"
        return self.message

    class Meta:
        ordering = ['-id']

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = '메세지 글자수'

class Comment(models.Model):
    post = models.ForeignKey('instagram.Post', 
                             on_delete=models.CASCADE,
                             limit_choices_to={'is_public' : True},)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post)
    
    def __str__(self):
        return self.name