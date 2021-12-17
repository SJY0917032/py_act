# 4-6

## Generic display View

`DetailView`

- 1개 모델의 1개 Ojbect에 대한 템플릿 처리
  - 모델명 소문자이름의 model instance를 템플릿에 전달
    - 지정 PK 혹은 slug에 대응하는 model instanced

`ListView`

- 1개 모델에 대한 List 템플릿 처리
  - 모델명소문자_list이름의 QuerySet을 템플릿에 전달
- 페이징 처리

```Python
post_list = ListView.as_view(model=Post, paginate_by=10)

'''
이런식으로 paginate_by = int 를 추가하면 자동으로 페이징이 생성된다
'''
```

**[장고 부트스트랩 4 라이브러리](https://django-bootstrap4.readthedocs.io/en/latest/)**

```Python
    # 사용하는 템플릿에 
    {% load bootstrap4 %} 를 추가한다.


    {% if is_paginated %}
        {% bootstrap_pagination page_obj justify_content="center" %}
    {% endif %}

    이런식으로 부트스트랩라이브러리를 사용해서 페이징처리를 손쉽게 할수있다.
```