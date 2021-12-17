# 3-3  

## Django - Admin  

django.contrib.admin 앱을 통해 제공된다.  
`/admin` : 실제 서비스에서는 다른주소로 변경 권장  
혹은 `django-admin-honeypot` 앱을 통해 가짜 admin페이지 노출  

모델 클래스 등록을 통해, 조회/추가/수정/삭제 웹 UI를 제공  
  서비스 초기에 관리도구로 사용하기에 제격  
  관리도구 만들 시간을 줄이고 End-User 서비스에 집중.  

내부적으로 DjangoForm을 적극적으로 사용

## 모델클래스를 admin에 등록하기

`등록법_1`

```Python
admin.site.registrt(Item) # 기본 ModelAdmin으로 동작
```  

`등록법_2`

```Python
class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin) #지정한 ModelAdmin으로 동작
```

`등록법_3`

```Python
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
```

## 모델 클래스에 __str__ 구현

객체를 출력할때, 객체.__str__()의 리턴값을 활용

str(..)은 자바의 toString과 유사하다.  

```Python
    # Java의 toString과 유사
    def __str__(self):
        # return f"custom Post Obejct ({self.id})"
        return self.message
```

## list_display, list_display_links

```Python
@admin.register(Post) # 파이썬의 장식자 문법 Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length','created_at','updated_at']
    list_display_links = ['message']
    
    #  이런식으로 model말고 admin에서도 구현이 된다.
    def message_length(self, post):
        return f"{len(post.message)} 글자"
    message_length.short_description = '메세지 글자수'
```

모델리스트에 출력한 컬럼을 지정할수 있다. 이는 models.py에 지정해도되고  
특정한곳에서만 사용한다면(admin등등..)admin에 등록해도 된다.  

또한 `list_display_links = ['message']`로  detail 링크를 걸 속성을 지정할수 있다.

## serach_fields 
**`admin내 검색UI를 통해 DB릁 롱한 where쿼리 대상 필드 리스트`**

```Python
search_fields = ['message']
```

## list_filter 속성
**`지정 핕드 값으로 필터링 옵션 제공`**

```Python
list_filter = ['created_at', 'is_public']
```
