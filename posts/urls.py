from django.urls import include, path
from .views import newPostView , singlePostView, editPostView

urlpatterns = [
    path('new/',newPostView,name="newPostView" ),
    path('<int:id>/',singlePostView,name="singlePostView" ),
    path('<int:id>/edit/',editPostView,name="editPostView" ),
    # path('delete/',logoutView,name="logoutView" ),
]
