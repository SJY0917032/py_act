# 3-1

## 장고 ORM

데이터 베이스에 쿼리하기 위한 언어 `SQL`
같은 작업을 하더라도 보다 적은수의 SQL  
보다 높은 성능의 SQL  
직접 SQL을 맏늘기도하지만 ORM을 통해 SQL을 생성 / 실행하기도 한다.  
`중요`  
**ORM을 쓰더라도 내가 작성된 ORM 코드를 통해 어떤 SQL이 실행되고 있는지 파악을 하고 이를 최적화 할 수 있어야한다.**  
-> `Django-debug-toolbar`를 적극 활용한다.  

장고 ORM인 Model은 RDB만을 지원한다  
**`MySQL`, `Oracle`, `postgreSQL`, `SqlLite3`**

## Django Model

`데이터베이스 테이블` - `파이썬 클래스`를 1:1로 매핑
모델 클래스명은 단수형으로 지정  
ex : Posts(x), Post(o)  
클래스 이기에 필히 첫 글자가 대문자인 파스칼케이스로  
서비스에 맞는 데이터베이스 설계가 필수  
이는 RDBMS에대한 학습이 필요한 EU

## Django Model 활용 순서

`장고 모델을 통해 DB형상을 관리 하는 경우`

1. 모델 클래스 작성  
2. 모델 클래스로부터 마이그레이션 파일 생성 `makemigrations`  
3. 마이그레이션 파일을 DB에 적용 `migrate`  
4. 모델 활용  

`장고 외부에서 DB형상을 관리 하는 경우`  

1. 데이터베이스로 부터 모델 클래스 소스 생성 `inspectdb`
2. 모델 활용  

## 모델명과 DB 테이블명

DB 테이블명 : Default -> '앱이름_모델명'  
EX:
  blog App  
  Post Model : 'blog_post'  
  Comment Model : 'blog_comment'  
  shop App  
  item Model : 'shop_item'  
  Review Model : 'shop_review'  
커스텀 지정 : 모델 Meta클래스의 db_table속성
  
## 적용순서

1. 아이템 모델 정의 `models.py`
2. 마이그레이션 파일 생성 `manage.py make~`
3. 마이그레이션 파일 적용 `manage.py migrate`
4. db확인  
