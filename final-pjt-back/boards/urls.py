from django.urls import path
from . import views

urlpatterns = [
    path('boards/',views.board_list),
    path('boards/<int:board_pk>/',views.board_detail),
    path('boards/<int:board_pk>/delete/',views.board_delete),
    path('boards/<int:board_pk>/comment/',views.comments_create),
    path('boards/<int:board_pk>/comment_list/',views.comment_list),
    path('boards/<int:board_pk>/<int:comment_pk>/delete/',views.comment_delete)
]
