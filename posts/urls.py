from django.urls import include, path
from .views import newPostView

urlpatterns = [
    path('new/',newPostView,name="newPostView" ),
    # path('/:id',loginView,name="loginView" ),
    # path('edit/:id',signupView,name="signupView" ),
    # path('delete/',logoutView,name="logoutView" ),
]
