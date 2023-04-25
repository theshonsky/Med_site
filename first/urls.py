from django.urls import path
from . import views 

urlpatterns = [
    path('main/', views.mainpage, name = 'mainpage'),
    path('sign_in/', views.sign_in, name = 'sign_in'),
    path('logout/', views.logoutuser, name = 'logout'),
    path('medcard/', views.medcard, name = 'medcard'),
    path('addcard/', views.addcard, name = 'addcard'),
    path('mkb10/', views.Mkb_10, name = 'mkb_10'),
    path('search/', views.searchcard, name = 'searchcard'),
    path('searchmkb/', views.searchmkb, name = 'searchmkb'),
    path('<int:pk>/direction',views.GeneratePdf.as_view(), name='direction'),
    path('<int:pk>',views.CardDetailView.as_view(), name='studmedcard'),
    path('<int:pk>/update',views.CardUpdateView.as_view(), name='card_update'),
    path('<int:pk>/delete',views.CardDeleteView.as_view(), name='card_delete')
]