"""
URL configuration for bookmyshow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home,name="home"),
    path('language/<name>',LanguageFilter),
    path('format/<name>',FormatFilter),
    path('genres/<name>',GenresFilter),
    path('category/<name>',CategoryFilter),
    path('movie/<id>',MovieDetails),
    path('signup',SignUp),
    path('signin',SignIn),
    path('signout',SignOut),
    path('search',Search),
    path('profile',Profile),
    path('submit_rating', SubmitRating),
    path('book_seat',BookSeat),
    path('paynow',PayNow),
    path("payment_success",PaymnetSuccess),
    path("paymnet_failed",Paymnetfailed),
    
    path('viewpdf/<id>',ViewPDF),
    path('downlaodpdf/<id>',DownlaodPDF)
    

] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

