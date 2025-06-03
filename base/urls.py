from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import Home, Signup, Signin, Signout, createArticle, ArticleView, UserProfile

urlpatterns = [
    path('', Home, name='home'),
    path('me/', UserProfile, name='user_profile'),
    # path('articles/', Articles, name='articles'),
    path('signup/', view=Signup, name='signup'),
    path('signin/', view=Signin, name='signin'),
    path('signout/', view=Signout, name='signout'),
    path('create/', view=createArticle, name='create_article'), 
    path('article-detail/<int:pk>/', ArticleView, name='article_detail'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)