from django.urls import path
from tapp import views

urlpatterns = [
    path('', views.demo, name='demo'),
    # path('About/', views.about, name='about'),
    # path('Contact/', views.contact, name='contact'),
    # path('gallery/', views.gallery, name='gallery'),
    # path('Pooja/', views.pooja, name='pooja')
]
