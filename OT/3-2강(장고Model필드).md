# 3-2

## 기본 지원되는 모델필드
`PK` : AutoField, BigAutoField  
`문자열` : CharField, TextField, SlugField  
`날짜/시간` : DateTimeField, DateField, TimeField  
`참/거짓` : BooleanField, NullBooleanField  
`숫자` : IntegerField, SmallIntegerField, PositiveIntegerField, PositiveSmallIntegerField, BigIntegerField, DecimalField, FloatField  
`파일` : BinaryField, FileField, ImageField, FilePathField  
`이메일` : EmailField  
`URL` : URLField  
`UUID` : UUIDField  
`아이피` : GenericIPAddressField  
`그리고 다양한 커스텀 필드들..` : [라이브러리](https://django-model-utils.readthedocs.io/en/latest/index.html)

## 모델필드들은 DB 필드 타입을 반영한다.
Varchar필드타입 -> CharField, SlugField, URLField, EmailField 등등..  
파이썬 데이터 타입과 데이터 베이스 데이터타입을 매핑한다.  
같은 모델필드라 할지라도 DB에 따라서 다른 타입이 될 수도 있다

## 자주쓰는 필드 공통 옵션
`blank` : validation시에 empty 허용 여부 (default : False)  
`null` : db옵션, null 허용여부 (default : False)  
`db_index` : db옵션, indexField 여부 (default : False)  
`default` : 디폴트값 지정  
`unique` : 현재 테이블 내에서 유일성 여부 (DB옵션)  
`choices` : select 박스 소스로 사용  
`validators` : validators를 수행할 함수를 다수 지정  
모델필드에 따라 고유한 validators들이 등록 ( ex : 이메일만 받기)  
`verbose_name` : 필드 레이블, 미지정시 필드명이 사용된다.  
`help_text` : 필드입력 도움말

## 중요
**`설계한 데이터 베이스 구조에 따라, 최대한 필드타입을 타이트하게 지정해야한다`**  

1. blank/null 지정은 최소화 해야한다.
2. validators들이 다양하게 타이트하게 지정된다.
3. 필요하다면 validators들을 추가로 타이트하게 지정해야한다.
4. 프론트엔드에서의 유효성검사는 사용자 편의를 위한것
5. 백엔드에서의 **유효성검사**는 필수
6. 직접 유효성 로직을 만들지말라 이미 잘 구성된 셋을 가져다 써라. 특히 장고의 Form/Model을 통해 지원되며 Serializer(djangoRestApi)를 통해서도 지원된다.  

  ORM은 SQL 쿼리를 만들어주는 역할일뿐 보다 성능 높은 어플리케이션을 위해서는 DB에대한 이해가 필요하다.  