from django.urls import include, path
from .views import indexView,loginView,signupView,logoutView,profileView,profileEditView

urlpatterns = [
    path('', indexView,name="indexView"),
    path('login/',loginView,name="loginView" ),
    path('signup/',signupView,name="signupView" ),
    path('logout/',logoutView,name="logoutView" ),
    path('profile/',profileView,name="profileView" ),
    path('profile/edit/',profileEditView,name="profileEditView"),
]
