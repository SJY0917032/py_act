# 6-2

## 장고에 가장 중요한 Feature

`주요 역할`

- 입력폼 HTML 생성
- 입력폼 값에 대한 유효성 검증 및 값 변환
- 검증을 통과한 값들을 Dict 형태로 제공.

## `Form` 처리

- 하나의 URL (하나의 View)에서 2가지 역할을 모두 수행
  - 빈 폼을 보여주는 역할
  - 폼을 통해 입력된 값을 검증하고 저장하는 역할.

`GET`

- New/Edit 입력폼을 보여줌

`POST`

- 데이터를 입력받아 (request.POST, request.FILES) 유효성 검증
- 검증 성공시 : SUCCESS URL로 이동
- 오류 메세지와 함께 입력폼을 다시 보여줌

## 필드별로 유효성 검사 함수 추가 적용

`함수로 유효성 검사가 가능하며`  

`Model단에서도 유효성 검사가 가능하다.`


## POST 요청에 한해서 입력값 유효성 검증을한다.

```Python
def post_new(request):
    if request.method == 'POST':
        # POST 인자는 request.POST와 request.FILES를 받음
        form = PostForm(request.POST, request.FILES)
        # 인자로 받은값에 대해서 유효성 검증 수행
        if form.is_valid(): # 검증 성공시 True
            # 검증에 성공한 값을 제공받으면 Django Form의 역할은 여기까지
            # 필요에따라 DB에 저장
            post = form.save() 
            return redirect(post)
    else :
        form = PostForm()
        
    return render(request, 'instagram/post_form.html', {
        'form': form,
    })
```

## 템플릿을 통한 HTML 폼 노출

`GET`

- 유저가 Form을 채우고 submit -> POST

`POST`

- form instance를 통해 HTML 폼 출력
- 오류메세지도 있다면 같이 출력
  - 유저가 Form을 채우고 submit -> POST 재요청

## Form Fields

`Model Fieds와 유사`

- Model : DB Field를 파이썬 클래스화
- Form : HTML Form Field를 파이썬 클래스화