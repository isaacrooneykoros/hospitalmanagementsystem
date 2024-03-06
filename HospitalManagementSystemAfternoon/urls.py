
from django.contrib import admin
from django.urls import path,include
from hospitalapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inner/', views.inner,name='inner'),
    path('login/', views.login,name='login'),
    path('register/', views.register,name='register'),
    path('details/', views.details,name='details'),
    path('adminhome/', views.adminhomme,name='adminhome'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimages/', views.showimages, name='showimages'),
    path('imagedelete/<int:id>', views.imagedelete),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),


]
