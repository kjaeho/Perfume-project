from django.urls import path
from . import views

app_name = 'perfumes'

urlpatterns = [
    path('recent-list/<int:page_num>/',views.recentList, name="perfume"),
    path('listby-category/<int:gender>/<str:brand>/<str:line>/<int:page_num>/',views.listBy),
    path('perfume/<int:perfume_id>/',views.perfumeDetail),
    path('listby-gender/<int:gender>/<int:page_num>/',views.genderList),
    path('listby-brand/<str:brand>/<int:page_num>/',views.brandList),
    path('listby-line/<str:line>/<int:page_num>/',views.lineList),
    path('search/<str:word>/<int:page_num>/',views.perfumeSearch),

    # 연령별 추천
    path('recommend/age/',views.byAgeRecommend),
    # path('recommend/age/social/',views.socialStudent),
    # path('recommend/age/30/',views.thirty),
    # path('recommend/age/40/',views.forty),
    # path('recommend/age/50/',views.fifty),
    path('recommend/weather/',views.weatherRecommend),
]
