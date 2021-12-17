# 5-5 

## Static & Media 파일

`Static` 파일 

- 개발 리소스로써 정적인 파일(js, css, image)
- 앱 / 프로젝트 단위로 저장 및 서빙

`Media`파일

- FileField / ImageField를 통해 저장한 모든 파일
- DB 필드에는 저장경로를 저장하며 파일은파일스토리지에 저장
- 프로젝트 단위로 저장/서빙

`장고 static 경로`

- 장고는 One Project, Multi App 구조
- 한 App을 위한 static 파일을 app/static/app 경로에 둔다.
- 프로젝트 전반적으로 사용되는 것은 settings.STATICFILES_DIRS에 둔다.
- 다수 디렉토리에 저장된 스태틱파일은 collectstatic 명령을 통해 지정한 경로로 모아서 서비스에 사용한다.

## Static Files Finders

`Template Loader`와 유사

- 설정된 Finders를 통해, static 템플릿이 있을 디렉토리 목록을 구성한다.
- 디렉토리 목록에서 지정 상대경로를 가지는 static파일을 찾는다.

`대표적인 2가지`

- `App Directories Finder`
- `File System Finder`


## 템플릿에서 static URL 처리 예시

`Template Tag를 통한 처리`

```Python
{% load static %}
<img src="{% static 'blog/title.png' %}"/>
# 프로젝트 설정에따라 유연하게 처리가능.
```

## 개발환경에서 static 파일서빙

`개발 서버를 쓰고 DEBUG가 True일때만 지원`

- 이는 순수 개발목적으로만 제공
- False일때는 별도로 static 서빙을 해야한다.

`URL을 통해 파일 시스템에 직접 접근하는것이 아니라.`  
`지정 이름의 STATIC 파일을 장고의 StaticFiles Finder에서`  
`대신 찾아 그 내용을 읽어서 응답하는 것`

## static 서빙을 하는 여러가지 방법

1. 클라우드 정적 스토리지나 `CDN`을 활용
2. apache/nginx 웹서버를 통한 서빙
3. 장고를 통한 서빙
   - whitenoise 라이브러리를 활용해서 가능 -> Heroku 배포에필요

## 외부 웹서버에 의한 static/media 컨텐츠 서비스

- 정적인 컨텐츠는 외부 웹서버를 통해 처리하면 효율적
- 정적컨텐츠만의 최적화된 방법을 사용해보자.
  - memcache/redis 캐시등..
  - CDN

## 배포시에 static 처리 프로세스

1. `서비스용 settings`에 배포 static 설정
2. 관련 클라우드 스토리지 설정, 혹은 아파치/nginx static 설정
3. 개발이 완료된 static 파일을 한 디렉토리로 복사
   1. `python manage.py collectstatic --settings=서비스용settings`
   2. `settings.STATIC_ROOT`로 복사됨
4. `settings.STATIC_ROOT`경로에 복사된 파일을 배포서버로 복사
   1. 대상 : `클라우드 스토리지`, `아파치/nginx`에 참조할 경로
5. `static` 웹서버를 가리키도록 `settings.STATIC_URL` 수정

## static 관련 라이브러리

`django-storages`

- Azure Storage, Amazon S3, Google Cloud Storage등등.. 지원

`django-storages-azure`

- azure용