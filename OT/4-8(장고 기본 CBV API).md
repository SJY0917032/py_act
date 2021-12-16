# 4-8

## ArchiveIndexView

`지정된 날짜필드 역순으로 정렬된 목록 (최신목록을 위한)`

- 필요한 URL 인자(없음)
  - 옵션: model,datefield,date_list_period(default:year)
- default Template_name_suffix : `_archive.html`
- Context
  - lastest : QuerySet
  - date_list : 등록된 Record의 년도 목록

## YearArchiveView

`지정 Year의 목록`

- 필요한 URL 인자(Year)
  - 옵션 : model,date_field
  - date_list_period : (defalut:month)
    - 지정 년도에서 month 단위로 Record가 있는 날짜 리스트
  - make_object_list(default : False)
    - 거짓일 경우 object_list를 비운다.

## Month, Day.. 

`지정 Month, Day의 목록`

- 필요한 URL 인자(Month or Day)
  - 옵션 : model,date_field
  - date_list_period : (defalut:month, day)
    - 지정 년도에서 month 단위로 Record가 있는 날짜 리스트
  - make_object_list(default : False)
    - 거짓일 경우 object_list를 비운다.

## Today

`오늘의 날짜 목록`

`Day와 유사하게 동작하지만 인자를 받지않는다.`

- previous_day, next_day를 미제공한다