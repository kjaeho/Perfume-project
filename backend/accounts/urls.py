from django.urls import path
from . import views


urlpatterns = [
    # path('', views.list),
    path("clothes/", views.clothes_get_create),
    path("clothes/<int:clothes_id>/", views.clothes_update_delete),
    path('join/<str:email>/',views.joinplus),
    path("userdetail/<str:email>/", views.userdetail),
    path("clothes/main/",views.clothes_get_main)
]
