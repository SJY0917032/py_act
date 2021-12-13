# 3-5

## Model Manager

데이터베이스 질의 인터페이스를 제공  
디폴트 Manager로써 ModelCls.objects 제공  



```Python
qs = Post.objects.all().order_by('-id')[:2]
print(qs.query)
```

`ORM의 쿼리를 부를때는 데이터가 필요한 시점에 쿼리를 Set하게 된다.`  
(출력이 필요할 때)

## QuerySest은 Chaining을 지원
Post.objects.all().filter(...).exclude(...).filter() -> QuerySet  
`QuerySet은 Lazy한 특성을 가진다.`  
QuerySet은 만드는 동안에 DB를 접근하지 않는다.  
**실제로 데이터가 필요한 시점에 접근을한다**

## 다양한 조회방법.
`.filter(...)` : QS  
`.exclude(...)` : QS  

`특정 모델객체 1개 획득을 할때.`  
queryset[숫자인덱스] -> 모델객체 혹은 예외발생 (indexError)  
queryset.get(...) -> 모델객체 혹은 예외발생 (DoesNotExist, MultipleObjectsReturned)  
queryset.first() -> 모델객체 혹은 None  
queryset.last() -> 모델객체 혹은 None

## Filter <-> exclude

인자로 필드명 = 조건값 지정  
1개 잏상의 인자 지정 -> 모두 `AND`조건으로 묶임  
`OR` 조건을 묶을려면, `django.db.models.Q` 활용

```Python
from django.db.models import Q

query = 'msg'

qs = Post.objects.all()
qs_or = qs.filter(Q(id__gte = 2) | Q(message__icontains=query)) # OR
qs_and = qs.filter(Q(id__gte = 2) & Q(message__icontains=query)) # AND
# and면 굳이 Q를 쓸필요가 없다.

# 이런식으로 | 나 &을 활용해서 ( || , &&이 아님!! )
# or나 and연산을한다
```

`방법을 바꾼다면`

```Python
from django.db.models import Q

query = 'msg'
qs = Post.objects.all()
cond = Q(id__gte = 2) | Q(message__icontains=query)
cond &= Q(...) # 이런식으로 조건을 추가할수있다.

qs_or = qs.filter(cond) # OR

```

## 필드 타입별 다양한 조건 매칭

`문자열 필드`  
`필드명__startwith = 조건값 -> 필드명 LIKE "조건값%"`  
`필드명__istartwith = 조건값 -> 필드명 ILIKE "조건값%"`  
`필드명__endtwith = 조건값 -> 필드명 LIKE "%조건값"`  
`필드명__iendtwith = 조건값 -> 필드명 ILIKE "%조건값"`  
`필드명__contains = 조건값 -> 필드명 LIKE "%조건값%"`  
`필드명__icontains = 조건값 -> 필드명 ILIKE "%조건값%"`  
ETC...  
