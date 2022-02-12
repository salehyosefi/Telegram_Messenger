from django.urls import path
from .views import GetAllData, EditData, PostModelData, SearchData

urlpatterns = [
    path('get-all-data/', GetAllData.as_view()),
    path('post-data/', PostModelData.as_view()),
    path('update-fav-data/<int:pk>', EditData.as_view()),
    path('search/', SearchData.as_view()),
    # path('chat/', index, name='index'),
    # path('<str:room_name>/', room, name='room'),
]