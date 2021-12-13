# 3-5

## Model Manager

데이터베이스 질의 인터페이스를 제공  
디폴트 Manager로써 ModelCls.objects 제공  

```Python
qs = Post.objects.all().order_by('-id')[:2]
print(qs.query)
```