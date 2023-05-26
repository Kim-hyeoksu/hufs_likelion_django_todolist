from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:pk>', views.todo_detail, name='todo_detail'), # 추가
    path('post/', views.todo_post, name='todo_post'), # 추가
    path('<int:pk>/edit/', views.todo_edit, name='todo_edit'), # 추가
    path('done/', views.done_list, name='done_list'), #추가
    path('done/<int:pk>/', views.todo_done, name='todo_done') #추가
]