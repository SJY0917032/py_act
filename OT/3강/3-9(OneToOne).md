# 3-9

## OneToOneField

`1 : 1` 관계에서 어느 쪽이라도 가능  
User:**`Profile`**  
FK(unique=True)와 유사하지만 reverse차이.  

- User:Profile을 `FK`로 지정한다면 -> profile.user_set.first() -> user
- User:Profile을 `OneToOne`으로 지정한다면 -> profile.user -> user

## O2O에서의 related_name

`reverse`접근시의 속성명 : 디폴트 -> 모델명소문자  

```Python
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)

# user.profile
# profile.user
```