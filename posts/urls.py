from django.urls import include, path
from .views import newPostView , singlePostView

urlpatterns = [
    path('new/',newPostView,name="newPostView" ),
    path('<int:id>/',singlePostView,name="singlePostView" ),
    # path('edit/:id',signupView,name="signupView" ),
    # path('delete/',logoutView,name="logoutView" ),
]
