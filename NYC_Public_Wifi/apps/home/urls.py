from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('search', views.search, name = 'search'),
    path('user_reviews/<int:pk>/', views.user_reviews, name = 'user_reviews'),
    path('search/<int:pk>/', views.hotspot_profile, name='hotspot_profile'),
    path('hotspot_profile/<int:pk>/', views.hotspot_profile, name='hotspot_profile'),
    path('hotspot_reviews/<int:pk>/', views.hotspot_reviews, name='hotspot_reviews'),
    path('hotspot_reviews/<int:pk>/add_review/', views.add_review, name='add_review'),
    

    ### add urls ###
    path('add_borough', views.add_borough, name='add-borough'),
    path('add_neighborhood', views.add_neighborhood, name='add-neighborhood'),
    path('add_provider', views.add_provider, name='add-provider'),
    
    ### update urls ###
    path('update_neighborhood/<ntacode>', views.update_neighborhood, name='update-neighborhood'),
    path('update_hotspot/<obj_id>', views.update_hotspot, name='update-hotspot'),
    path('update_provider/<prov_id>', views.update_provider, name='update-provider'),
    
    
    ### delet urls ###
    path('delete_neighborhood/<ntacode>', views.delete_neighborhood, name='delete-neighborhood'),
    path('delete_hotspot/<obj_id>', views.delete_hotspot, name='delete-hotspot'),
    path('delete_provider/<prov_id>', views.delete_provider, name='delete-provider'),
    
    
    ### list urls ###
    path('neighborhood_list', views.neighborhood_list, name='neighborhood-list'),
    path('hotspot_list', views.hotspot_list, name='hotspot-list'),
    path('provider_list', views.provider_list, name='provider-list'),
    
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
