from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="generalpage"),
    path('about/', about, name="aboutpage"),
    path('post/', post, name="postpage"),
    path('contact/', login_required(create_article), name="create_article"),

    path('<int:article_id>/', article_detail, name='article_detail'),
    path('article/<int:pk>/delete/', delete_article, name='delete_article'),
    path('article/edit/<int:article_id>/', edit_article, name='edit_article'),


    path('login/', login_view, name="login"),
    path('register/', sing_up, name="SingUp"),
    path('logout/', logout_view, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)