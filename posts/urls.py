from django.urls import include, path
from .views import newPostView , singlePostView, editPostView,deletePostView,getMorePostsView

urlpatterns = [
    path('new/',newPostView,name="newPostView" ),
    path('<int:id>/',singlePostView,name="singlePostView" ),
    path('<int:id>/edit/',editPostView,name="editPostView" ),
    path('<int:id>/delete/',deletePostView,name="deletePostView" ),
    path('getmore/',getMorePostsView,name="getMorePostsView" ),
]
