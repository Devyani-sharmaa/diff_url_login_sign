from django.urls import path
from ep import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('home/',views.HomePage,name='home'),
     path('submit/',views.submit)]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    