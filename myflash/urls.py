from django.urls import path, re_path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import FlashcardCreateView,FlashcardListView,FlashcardUpdateView,FlashcardDeleteView

urlpatterns=[
    path('',FlashcardListView.as_view(),name = 'index'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('post/new/', FlashcardCreateView.as_view(), name='post-create'),    
    path('post/<int:pk>/update/',FlashcardUpdateView.as_view(), name="updateForm"),
    path('post/<int:pk>/delete/',FlashcardDeleteView.as_view(), name="deleteForm"),
    path('search/cards', views.search_cards, name = 'search_cards'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)