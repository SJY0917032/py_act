# 4-9

## HTTP 상태코드

**웹서버는 적절한 상태코드로써 응답해야한다.**  
**각 `HttpResponse` 클래스마다 고유한 `status_code`가 할당된다**  
**`REST API`를 만드는데 특히 유용**  

## 대표 코드

`200번대 (성공)`

- 200 : 서버가 요청 처리 OK
- 201 : 작성됨, 서버가 요청을 접수하고 새 리소스를 작성했다.

`300번대 (요청을 마치기위해 추가 조치필요)`

- 301 : 영구 이동(요청한 페이지가 새 위치로 영구적으로 이동)
- 302 : 임시 이동(페이지가 현재 다른 위치에서 요청에 응답하고 있지만 요청자는 향후 원래 위치를 사용해야만 한다.)

`400번대 (클라이언트 Error)`

- 400 : 잘못된 요청
- 401 : 권한 없음
- 403 : 필요한 권한이 없다
- 404 : 서버에 리소스가 없다
- 405 : 허용되지 않는방법 EX : GET -> POST

`500번대 (서버 Error)`

- 500 : 서버 내부 오류 발생
