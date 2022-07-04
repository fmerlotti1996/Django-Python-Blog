from django.urls import path
#from .import views
from .views import AddPostView, HomeView,ArticleDetailView,UpdatePostView,DeletePostView,AboutView,PagesView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',HomeView.as_view(), name = "home"),
    path('home/',HomeView.as_view(), name = "home"),
    path('pages/',PagesView.as_view(), name = "pages"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = "article_details"),
    path('add_post/',AddPostView.as_view(), name = "add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name = "update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name = "delete_post"),
    path('about/', AboutView.as_view(),name = "about"),
]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)