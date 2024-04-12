from django.urls import path
from .views import *

urlpatterns = [
    path('verify/<int:user_pk>/<str:token>/', VerifyEmailView.as_view(), name='verify'),
    path('',Home.as_view(), name='home'),
    path('search/',Search.as_view(),name='search'),
    path('search/homework/',Search1.as_view(),name='search1'),
    path('index/',Index.as_view(), name='index'),
    path('signup/', SingUpView.as_view(), name='signup'),
    path('login/',Login.as_view(), name='login'),
    path('logout/',Logout.as_view(), name='logout'),
    path('book/create/',CreateBook.as_view(), name='create_book'),
    path('book/<int:pk>/',BookDetail.as_view(), name='book_detail'),
    path('book/<int:pk>/update/',UpdateBook.as_view(), name='update_book'),
    path('book/<int:pk>/delete/',DeleteBook.as_view(), name='delete_book'),
    path('book',BookList.as_view(),name='book_list'),
    path('homework',HomeWorkList.as_view(),name='homework_list'),
    path('homework/<int:pk>/',HomeWorkDetail.as_view(),name='homework_detail'),
    path('homework/<int:pk>/update/th/',UpdateHomeWorkTeacher.as_view(),name='homework_update_th'),
    path('homework/<int:pk>/update/st/',UpdateHomeWorkStudent.as_view(),name='homework_update_st'),
    path('homework/create/th/',CreateHomeWorkTeachers.as_view(),name='homework_create_th'),
    path('homework/create/st/',CreateHomeWorkStudents.as_view(),name='homework_create_st'),
    path('homework/<int:pk>/delete/',DeleteHomeWork.as_view(),name='homework_delete'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('exam/',Exam.as_view(),name='exam'),
    path('mark/',Mark.as_view(),name='mark'),
    path('schedules/',Schedules.as_view(),name='schedule'),

]
