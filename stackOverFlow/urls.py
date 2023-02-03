from django.contrib import admin
from django.urls import path
from home import userViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userRegestration',userViewSet.UserViewSet.userRegistration),
    path('userLogin',userViewSet.UserViewSet.userLogin)
]
