from django.urls import path

from . import views

app_name = "forum"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:board_name>/", views.boards, name="boards"),
    path("posts/<int:post_id>/", views.posts, name="posts"),

    ## HTMX stuff
    
    path("<str:board_name>/new-post/", views.new_post, name="new-post"),
    path("<str:board_name>/post_list/", views.post_list, name="post-list"),
    path("posts/<int:post_id>/new_comment/", views.new_comment, name="new-comment"),
    path("posts/<int:post_id>/comment_list/", views.comment_list, name="comment-list"),
]