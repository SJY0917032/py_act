from django.urls import path,re_path,register_converter
from . import views

class YearConverter:
    regex = r"20\d{2}"
    
    def to_python(self, value):
        return int(value)
    
    def to_url(self, value):
        return str(value)


register_converter(YearConverter, 'year')


app_name = 'instagram' # URL Reverse에서 namespace 역할을 한다.

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail),
    
    # path('acrhives/<int:year>/', views.achives_year),
    # 일반 path
    
    # re_path('archives/(?P<year>20\d{2})/', views.achives_year),
    # 정규표현식 path
    
    path('acrhives/<year:year>/', views.achives_year),
    # register_converter를 활용한 path (커스텀 컨버터)
]
