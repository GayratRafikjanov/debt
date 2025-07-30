from django.contrib import admin
from django.urls import path, include
from .apis import (UserListView, UserCreateView,
                   UserDeleteView, UserUpdateView, UserDetailView)

app_name = 'users'


urlpatterns = [
    path('users/list/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:user_id>/update/', UserUpdateView.as_view(), name='user-delete'),
    path('users/<int:user_id>/detail/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:user_id>/delete/', UserDeleteView.as_view(), name='user-update'),
]

