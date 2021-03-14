from django.urls import include, path
from .views import indexView,loginView,signupView,logoutView,profileView,profileEditView,changePasswordView

urlpatterns = [
    path('', indexView,name="indexView"),
    path('login/',loginView,name="loginView" ),
    path('signup/',signupView,name="signupView" ),
    path('logout/',logoutView,name="logoutView" ),
    path('changepassword/',changePasswordView,name="changePasswordView"),
    path('profile/edit/',profileEditView,name="profileEditView"),
    path('<str:usr>/',profileView,name="profileView" ),
]
