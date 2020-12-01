from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    #review
    path('<int:user_id>/review-list/',views.review_list),
    path('<int:review_id>/review-detail/',views.review_detail),
    path('create-review/',views.create_review),
    path('<int:review_id>/update-review/',views.update_review),
    path('<int:review_id>/delete-review/',views.delete_review),
]
