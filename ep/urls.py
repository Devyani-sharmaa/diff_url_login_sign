from django.urls import path
from ep import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('home/',views.HomePage,name='home'),
    path('submit/',views.submit),
    path("add_product",views.add_product),
    # path('', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    # path('data', views.pivot_data, name='pivot_data'),
    ]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    