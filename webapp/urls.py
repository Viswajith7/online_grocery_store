from django.urls import path
from webapp import views

urlpatterns = [
    path('webpage/', views.webpage, name="webpage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('productpage/', views.productpage, name="productpage"),
    path('productpage/', views.productpage, name="productpage"),
    path('shoppage/<catg>/', views.shoppage, name="shoppage"),
    path('singleproduct/', views.singleproduct, name="singleproduct"),
    path('singleproduct/<int:dataid>/', views.singleproduct, name="singleproduct"),
    path('userloginpage/', views.userloginpage, name="userloginpage"),
    path('savelogin/', views.savelogin, name="savelogin"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),

    path('savecart/', views.savecart, name="savecart"),
    path('displaycart/', views.displaycart, name="displaycart"),
    path('checkout/', views.checkout, name="checkout"),


]
