# 4-10

## URL Dispatcher

`urls.py` 변경만으로 각 뷰에대한 URL이 변경되는 유연한 URL 시스템  

`URL Reverse의 효과`

- 개발자가 일일히 URL을 계산하지 않아도된다.
  - 만약 `<a href="blog"/>` 이런식으로 코딩을하면 일일히 수정해야한다.
- 장고에게 위임한다.

## URL Reverse를 수행하는 4가지 함수

`url 템플릿태그`

- 내부적으로 reverse 함수를 사용

`reverse 함수`

- 매칭 URL이 없으면 NoReverseMatch 예외 발생

`reslove_url 함수`

- 매핑 URL이 없으면 `인자 문자열`을 그대로 리턴
- 내부적으로 reverse 함수를 사용

`redirect 함수`

- 매칭 URL이 없으면 `인자 문자열`을 그대로 URL로 사용
- 내부적으로 resolve_url 함수를 사용


## 사용 예

```Python

blog => appname
post_detail => urlpatterns_name

{% url 'blog:post_detail' 100 %} => 문자열 URL
{% url 'blog:post_detail' pk=100 %} => 문자열 URL

reverse('blog:post_detail', args=[100]) => 문자열 URL
reverse('blog:post_detail', kwargs={'pk' : 100}) => 문자열 URL

resolve_url('blog:post_detail', 100) => 문자열 URL
resolve_url('blog:post_detail', pk = 100) 
resolve_url('/blog/100/') 

redirect('blog:post_detail', 100) => HttpResponse 응답 ( 301 or 302 )
redirect('blog:post_detail', pk = 100)
redirect('/blog/100/')

```

## 모델 객체에 대한 detail 주소 계산

**`매번 위와 같은 코드로 할수 있지만.`**  
**`아래와 같이 사용할 수 도 있다`**

- `resolve_url(post)`
- `redirect(post)`
- `{{ post.get_absolute_url }}`


## 모델 클래스에 get_absolute_url() 구현

- resolve_url 함수는 가장 먼저 get_absolute_url() 함수의 존재여부를 체크하고,
- 존재할 경우 reverse를 수행하지 않고 그 리턴값을 즉시 리턴

## 그 외 활용

- CreateView, UpdateView
  - success_url을 제공하지 않는 경우 해당 model instance의 get_absolute_url로 이동이 가능한지 체크하고 이동이 가능할 경우 이동
  - 생성/수정 하고나서 Detail화면으로 이동하는것은 매우 자연스러운 시나리오
- 특정 모델에 대한 Detail뷰를 작성할 경우
  - Detail뷰에 대한 URLConf설정을 하자말자, 필히 **`get_absolute_url`** 설정을 하자 코드가 보다 간결해진다.

