from django.conf import settings
from django.conf.urls.static import static

from . import views
from Rakes.views import createvieww
from django.urls import path



urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('createform/',createvieww.as_view(),name='createview'),
    path('Product',views.product,name='product')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

