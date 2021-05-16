from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "PARTY ZONE PAWNA LAKE CAMPING"
admin.site.site_title = "ADMIN | PARTY ZONE PAWNA LAKE CAMPING"
admin.site.index_title = "ADMIN PANEL"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('faq/', views.faq, name='faq'),
    path('refund/', views.refund, name='refund'),
    path('termsandcond/', views.termsandcond, name='termsandcond'),
    path('blog/', views.blog, name='blog'),
    path('<str:slug>', views.blogPost, name='blogPost')
]