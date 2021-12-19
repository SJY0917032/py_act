# 6-1

## Django Form(서버) <-> HTML Form(클라이언트)

Django -> 클라이언트로부터 전달받은 값들에 대한 유효성 검사를 수행하고
이를 데이터베이스에 저장하는 등의 처리를 한다.

## HttpRequest 객체

클라이언트로 부터의 모든 요청내용을 담고있다.

`함수기반뷰` : 매 요청시마다 첫번째 인자 request로 전달
`클래스기반뷰` : 매 요청 시마다 self.request로 접근

`form 처리 관련 속성들`

- .method : 요청의 종류 `GET`, `POST`로 모두 대문자
- .get : `GET`인자 
- .post : `POST`인자
- .FILES : POST인자중 파일목록 (MultiValueDict)

## MultiValueDict

`dict`를 상속받은 클래스  
`동일 Key`의 `다수 Value`를 지원하는 사전  
`수정이 불가능하다.`  


## HttpResponse

`다양한 응답을 Warpping`

- View에서는 반환값으로써 HttpResponse 객체를 기다린다.

## JsonResponse

`클라이언트가 요청했을때 응답을 줄때 다양한 포맷을 정할 수 있다.`  
`DRF에선 Renderer라고 일컫는다.`


## FileResponse

`StrineamingHttpResponse`를 상속받음  

- 파일 내용 응답에 최적화
- Content-Length, Content-Type, Content-Disposition헤더를 자동지정

`인자`  

- openfile, as_attachment, filename