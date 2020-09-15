from django.urls import path
from .views import *

app_name="post"
urlpatterns = [
    path('',post_list,name='post_list'),
    path('post/<int:pk>/',post_detail,name='post_detail'),
    path('post/create/',post_new,name='post_new'),
    path('post/edit/<int:pk>/',post_edit,name='post_edit'),
    path('post/drafts/',post_draft_list,name='post_draft_list'),
    path('post/<int:pk>/publish/',post_publish,name='post_publish'),
    path('post/<int:pk>/delete/',post_remove,name='post_remove'),
    path('post/<int:pk>/comment/',add_comment_to_post,name='add_comment_to_post')
]