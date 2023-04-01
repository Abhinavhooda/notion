from django.urls import path,re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from webnotion import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('contactform', views.contactform, name='contactform'),
    path('career/', views.career, name='career'),
    path('faqs/', views.faqs, name='faqs'),
    path('newsletter/', views.newsletter, name='newsletter'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404= 'webnotion.views.handler404'