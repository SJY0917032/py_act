# 5-3

## JS

`V8`엔진을 오픈소스로 공개

- 이를 통해 node.js플랫폼이 개발됐다

## Jquery

- 최근에는 별로안씀
- 무거워졌지만 방대하다
- 웹 페이지 개념에선 먹히던 라이브러리
- 요즘은 웹앱의 개념이기에 한물지나감.

## 구현해볼 기능

1. Event Listener 등록
2. DOM 엘리먼트 추가 및 제거
3. Ajax Get / Post


## Ajax GET/ POST

- HTTP 
  - GET : 주로 검색/조회/페이징
  - POST : 수정/삭제
- CORS를지원 (서버측셋업이 필요, 장고는 `django-cord-headers`)
- Django View에서는 POST를 받을 때 CSRF Token값을 체크
  - CSRF Token값이 없거나 맞지않으면 400에러를 뱉는다
  - Django에서의 대응은 공식문서 참고. 