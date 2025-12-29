from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("page/",views.MyPage,name="Mypage"),
    # path("about/",views.About,name="AdminPage"),
    # path("form/",views.Forms,name="FormPage"),
    # path("calculator/",views.Calcul,name="calcu"),
    # path("marksheet/",views.Marks,name="marks"),
    path("home/", views.index,name="tweethome"),
    path("tweet/", views.tweet_list,name="tweet_list"),
    path("create/", views.tweet_create,name="tweet_create"),
    path("<int:t_id>/edit/", views.tweet_edit,name="tweet_edit"),
    path("<int:t_id>/delete/", views.tweet_delete,name="tweet_delete"),
    path("register/", views.register,name="register"),

]
