# 4-5

## Built-in CBV API

`Base Views`

- view, TemplateView, RedirectView

`Generic display views`

- DetailView, ListView

`Generic date Views`

- ArchiveIndexView, Year..., Month..., Week..., Day..., Today..., DateDetailView

`Generic editing views`

- FormView, CreateView, UpdateView, DeleteView


## Base Views

`View`  

`TemplateView`
(TemplateResponseMixin, ContextMixin, View)  

`RedirectView`
(View)  

## View

모든 CBV의 모체 ( 이 CBV를 직접 쓸 일은 거의 없다 )  
http method별로 지정 이름의 멤버 함수를 호출하도록 구현  
`CBV.as_view(**initkwargs)`


## RedirectView

`permanent`

- True(301) -> 영구적인 이동(검색엔진에 영향)
- False(302) -> 임시이동

`url` (None)  

- url 문자열

`pattern_name` (None)

- url Reverse를 수행할 문자열

`quert_string` (False)

- QueryString을 그대로 넘길것인지 여부