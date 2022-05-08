from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('search', views.search, name = 'search'),
    path('search/<int:pk>/', views.hotspot_profile, name='hotspot_profile'),
    path('hotspot_profile/<int:pk>/', views.hotspot_profile, name='hotspot_profile'),
    path('hotspot_reviews/<int:pk>/', views.hotspot_reviews, name='hotspot_reviews'),
    path('hotspot_reviews/<int:pk>/add_review/', views.add_review, name='add_review'),
    path('user_reviews', views.user_reviews, name = 'user_reviews'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
