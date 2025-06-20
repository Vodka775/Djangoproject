"""
URL configuration for secondproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from secondapp.views import addProduct, addQuestion, addUser, deleteProduct, deleteQuestion, display, endexam, getAllProducts, getAllUsers, getAllquestion, getProduct, getUser,giveMeLogin, giveMeRegister, login, nextQuestion, previousQuestion,register, sendData,startTest, updateProduct, updateQuestion, updateUser, viewQuestion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('display/',display),
    path('addQuestion/', addQuestion),
    path('viewQuestion/',viewQuestion),
    path('deleteQuestion/',deleteQuestion),
    path('updateQuestion/',updateQuestion),
    path('giveMeRegister/',giveMeRegister),
    path('giveMeLogin/',giveMeLogin),
    path('login/',login),
    path('register/',register),
    path('startTest/',startTest),
    path('nextQuestion/',nextQuestion),
    path('previousQuestion/',previousQuestion),
    path('startTest/',startTest),
    path('endexam/',endexam),
    path('sendData/',sendData),
    path('getAllUsers/',getAllUsers),
    path('getAllquestions/', getAllquestion),
    path('getUser/<username>',getUser),
    path('addUser/',addUser),
    path('updateUser/',updateUser),
    path('getAllProducts/', getAllProducts),
    path('getProduct/<int:product_id>/', getProduct),  
    path('addProduct/', addProduct),
    path('updateProduct/', updateProduct),
    path('deleteProduct/<int:id>/', deleteProduct),
  
    

]
