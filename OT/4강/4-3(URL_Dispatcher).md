# 4-3

## URL Dispatcher

`특정 URL 패턴` -> View의 List

`프로젝트/settings.py`에서 최상위 `URLConf`모듈을 지정

- 최초의 `urlpatterns`로부터 include를 통해 TREE구조로 확장

`HTTP`요청이 들어올 때마다 등록된 `urlpatterns`상의 매핑 리스트를 처음부터 순차적으로 훑으며 URL 매칭을 시도

- 매칭이 되는 URL Rule이 다수 존재하더라도 처음의 Rule을사용
- 매칭되는 URL Rule이 없으면 404 Error를 발생시킨다.

`path() or re_path()`

- `re_path()`
  - django.conf.urls.url()과 동일하다.
- `path()`
  - 기본 지원되는 Path converters를 통해 정규표현식 기입이 간소화 (만능은 아님)
  - 자주 사용하는 패턴을 Converter로 등록하면 재활용 면에서 편리하다. 

## 새로운 장고앱을 생성할때 추천 작업

1. 앱 생성
2. 앱이름/urls.py 생성
3. 프로젝트/urls.py에 include 적용
4. 프로젝트/settings.py에 INSTALLED_APPS에 앱이름 등록.