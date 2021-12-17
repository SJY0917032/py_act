# 4-1

## View

1개의 `HTTP`요청에 대해 -> 1개의 `View`가 호출된다.  
`urls.py/urlpatterns`리스트에 매핑된 호출 가능한 객체  
함수도 `호출 가능한 객체`중에 하나  

`크게 2가지 형태의 뷰가 있다.`

- `함수 기반 뷰`
  - 장고 `View`의 기본
    - `호출 가능한 객체` 그 자체
  - 클래스 기반 `View`
    - `클래스.as_view()`를 통해 `호출 가능한 객체`를 생성/리턴
  
## View 호출시, 인자

- `HTTPRequest`
  - 현재 요청에 대한 `모든` 내역을 담고 있다.

- `URL Captured Values`
  - `url/re_path`를 통한 처리에는 -> 모든 인자는 STR로 전달
  - `path`를 통한 처리에서는 -> 매핑된 `Converter`의 `to_python`에 맞게 변환된 값이 인자로 전달된다.

## View 호출에 대한 리턴값 (HttpResponse)

`필히 HttpResponse` 객체를 리턴해야한다.

- 장고 Middleware에서는 `뷰`에서 `HttpResponse`객체를 리턴하기를 기다린다. (다른 타입을 리턴하면 처리오류)
- django.shortcuts.render 함수는 템플릿 응답을 위한 shortcut함수.

`파일like객체 혹은 str/byte타입의 응답 지원`

- str문자열을 직접 utf-8로 인코당힐 이유가 없다.
  - 장고 디폴트 설정에서 str 문자열을 utf-8로 인코딩한다.
- `response` = `HttpResponse` (파일like객체 또는 str객체 또는 byte객체)

`파일 like 객체`

- response.write(str 객체 또는 bytes 객체)