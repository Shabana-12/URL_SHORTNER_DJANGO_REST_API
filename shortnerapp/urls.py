
from django.urls import path

from django.urls import path
from . views import *


urlpatterns = [
    path('',ListTodoAPIView.as_view(),name='todo'),
    path('<str:pk>/detail',TodoDetailAPIView.as_view(),name='detail'),
    path('create',CreateTodoAPIView.as_view(),name='create'),
    path('<str:pk>/update',UpdateTodoAPIView.as_view(),name='update'),
    path('<str:pk>/delete',DeleteTodoAPIView.as_view(),name='delete'),
    # path('<str:shortener_link>/',Redirector.as_view(),name='redirector'),
]