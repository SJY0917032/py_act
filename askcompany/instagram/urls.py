from django.urls import path,register_converter
from . import views
from .converters import YearConverter, MonthConverter, DayConverter


register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')

app_name = 'instagram' # URL Reverse에서 namespace 역할을 한다.

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name="post_detail"),
    
    # path('acrhives/<int:year>/', views.achives_year),
    # 일반 path
    
    # re_path('archives/(?P<year>20\d{2})/', views.achives_year),
    # 정규표현식 path
    
    # path('acrhives/<year:year>/', views.achives_year),
    # register_converter를 활용한 path (커스텀 컨버터)
    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_year_archive'),
    # path('archive/<year:year>/<month:motnh>/', views.post_archive_month, name='post_month_archive'),
    # path('archive/<year:year>/<month:motnh>/<day:day>/', views.post_archive_day, name='post_day_archive'),
]
