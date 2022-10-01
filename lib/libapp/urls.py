from django.contrib import admin
from django.urls import path
from libapp import views

urlpatterns = [
    path('',views.index),
    path('library',views.create_work),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete_book),
    path('issuebook',views.book_issue),
    path('issuedbooks',views.book_issued),
    path('apj',views.DR_APJ),
    path('mohin',views.MOHIN),
    path('allbooks',views.ALL_BOOK),
    path('maharashtra',views.MAHARASHTRA),
    path('indian',views.INDIAN),
    path('netflix',views.NETFLIX),
    path('register',views.Register),
    path('login',views.Login),
    path('logout',views.Logout),
    path('getid',views.getlogonuserid),
    



]