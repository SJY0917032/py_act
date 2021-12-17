# 3-4

## Static & Media파일

`Static파일`  
개발 리소스로서의 정적인 파일(js,css,image등등..)  
앱 / 플젝 단위로 저장&서빙  

`Media파일`  
FileField/ImageField를 통해 저장된 모든 파일  
DB필드에는 저장 경로를 저장하며 파일은 파일 스토리지에 저장  
**`실제로 문자열을 저장하는 필드(중요)`**  
프로젝트 단위로 저장 & 서빙

## Media 파일 처리 순서

1. HttpRequest.FILES를 통해 파일이 전달
2. 뷰 로직이나 폼로직을통해, 유효성 검증을 수행하고
3. FileField/ImageField 필드에 **`경로`** 를 저장하고
4. settings.MEDIA_ROOT 경로에 파일을 저장한다.

## Media파일, 관련 settings 예시

각 설정의 Default값  

```Python
MEDIA_URL = ''
# 각 미디어 파일에 대한 URL Prefix
#필드명.url속성에 의해서 참조되는 설정

MEDIA_ROOT = ''
# 파일필드를 통한 저장 시에, 실제 파일을 저장할 ROOT경로 
```

## FillField와 ImageField

`FileField`  
File Storage API를 통해 파일을 저장  
장고에서는 File System Storage만 지원, django-storages를 통해 확장 지원  
해당 필드를 옵션 필드를 두고자 할경우, blank=True옵션 적용  

`ImageField` (FileField 상속)  
Pilow (이미지 처리 라이브러리)를 통해 이미지 width/height 획득  
위 필드를 상속받은 커스텀 필드를 만들수 있다  
ex : PDFField, ExcelField등등..

## 사용할만한 필드 옵션

`blank` : 업로드 옵션 처리 여부  
`upload_to` : MEDIA_ROOT 하위에서 저장한 파일명/경로명 결정  
**추천) 성능을 위해 한 디렉토리에 너무 많은 파일이 저장되지 않도록 조정**  
동일 파일명으로 저장시에, 파일명에 더미 문자열을 붙여 파일 덮어쓰기 방지

```Python
photo = models.ImageField(blank=True, upload_to='instagram/post/%Y%m%d')
# 이런식으로 %Y%m%d를 넣어서 년월일로 구분하게된다면 더빠른 처리가 가능하다.
```

## 파일 업로드시, HTML Form enctype

`form method는 필히 POST`  

## upload_to 인자

**`파일저장시에 upload_to 함수를 호출하여 저장경로를 계산`**  
파일 저장 시에 upload_to 인자를 변견한다고 해서, DB에 저장된 경로값이 갱신되진 않는다.  

`인자유형`

1. 문자열로지정(파일을 저장할 `중간 디렉토리 경로`로써 활용 가능)

2. 함수로지정 (`중간 디렉토리 경로` 및 `파일명`까지 결정 가능)

## 예시 _ uuid를 통한 파일명 정하기

```Python
import os
from uuid import uuid4
from django.utils import timezone

def uuid_name_upload_to(instance, filename):
    app_label = instance.__class__.meta.app_label # 앱별로
    cls_name = instance.__class__.__name__.lower() # 모델별로
    ymd_path = timezone.now().strftime('%Y/%m/%d') #업로드 하는 년/월/일별로
    uuid_name = uuid4().hex 
    extension = os.path.splitext(filename)[-1].lower() # 확장자 추출및 소문자 변환
    return '/'.join([
        app_label,
        cls_name,
        ymd_path,
        uuid_name[:2],
        uuid_name + extension,
    ])
```

## 템플릿에서 media URL 처리 예시

필드의 .url속성을 활용한다.  

내부적으로 settings.MEDIA_URL과 조합을 처리  
`<img src="{{post.photo.url}}" %}" />`  
필드에 저장된 경로에 없을 경우, .url 계산에 실패함에 유의 그러니 안전하게 필드명 저장유무를 체크  

```
{% if post.photo %}
    <img src="{{post.photo.url}}" %}" />
{% endif %}
```

## File Upload Handler

파일크기가 2.5mb 이하일 경우
메모리에 담겨 전달 
`MemoryFileUploadHandler`

파일크기가 2.5mb 이상일경우 디스크에 담겨 전달  
`TemporaryFileUploadHandler`  

관련 설정  
`settings.FILE_UPLOAD_MAX_MEMORY_SIZE`  
(Default 2.5MB)