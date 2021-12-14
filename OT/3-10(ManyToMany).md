# 3-10

## ManyToMany

`M : N`관계에서 어느 쪽이라도 필드 지정 가능  
`ManyToManyField(to, blank=False)`

```Python
    class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y%m%d')
    # 방법 1 사용하는곳에 ManyToManyField를 걸어준다
    tag_set = models.ManyToManyField('Tag', blank=True) # 태그가 없을수도 있기에 blank를 넣어줘야한다.
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post) 
    # 방법 2 M2M이 있는곳에 걸어준다.
    
    def __str__(self):
        return self.name
```

위와 같이 ManytoMany에서는 **`blank`** 로 지정하는것이 의미가있다

## o2o, fk, m2m

**`o2o`** 과 **`FK`** 는 두개의 테이블만 있어도 충분하지만  
**`M2M`** 는 두개의 테이블로는 정의가 불가능하다  
즉 중간의 **`Table`**이 필요하다.  
Django에선 ManyToManyField를 걸면 자동으로 생성해준다.

## RDBMS지만 DB따라 NoSQL도 지원한다.

`EX : 하나의 Post안의 다수의 댓글 저장 가능`  

**`djkoch/jsonfield`** 

- 대개의 DB엔진에서 사용 가능
- TextField/CharField를 래핑
- dict등의 타입에 대한 저장을 직렬화하여 문자열로 저장한다.
  - 내부 필드에 대해서는 쿼리 불가능

**`django.contrib.postgres.fields.JSONField`**

- 내부적으로 PostgreSQL의 jsonb타입
- 내부 필드에 대해 쿼리를 지원한다.

**`adamchainz/django-mysql`**

- MySQL 5.7이상에서 json필드 지원.