from django.urls import path
from . import views
from .views import submit_data, submit_image
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.landingpage,),
    path('home/',views.home, name='home'),
    path('text/',views.textmoderation, name='text'),
    path('image/',views.imagemoderation, name='image'),
    path('aboutme/',views.aboutme, name='aboutme'),
    path('submit/', submit_data, name='submit_data'),
    path('submitimage/', submit_image, name='submit_image'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    