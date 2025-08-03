from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.landing, name = 'landing'),
    path('signin/',views.signin, name = 'signin'),
    path('signup/',views.signup, name = 'signup'),
    path('signout/',views.signout, name = 'signout'),
    path('home/', views.home, name='home'),
    path('flipkart/', views.flipkart, name='flipkart'),
    path('wishlist_action/', views.wishlist_action, name='wishlist_action'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('flipkartwomen/',views.flipkartwomen,name = 'flipkartwomen'),
    path('flipkartmens/',views.flipkartmens,name = 'flipkartmens'),
    path('flipkartsports/',views.flipkartsports,name = 'flipkartsports'),
    path('flipkarthome/',views.flipkarthome,name = 'flipkarthome'),
    path('flipkartelec/',views.flipkartelec,name = 'flipkartelec'),

    path('amazon/', views.amazon, name='amazon'),
    path('amazonwomen/',views.amazonwomen,name = 'amazonwomen'),
    path('amazonmens/',views.amazonmens,name = 'amazonmens'),
    path('amazonsports/',views.amazonsports,name = 'amazonsports'),
    path('amazonhome/',views.amazonhome,name = 'amazonhome'),
    path('amazonelec/',views.amazonelec,name = 'amazonelec'),
    path('set_preference/',views.set_preference, name = 'set_preference')

]