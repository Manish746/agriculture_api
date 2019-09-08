from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    # Url for base user / auth user
    path('api/user/', views.UserList.as_view(), name='user-list'),
    path('api/get-user/', views.GetUser.as_view(), name='get-user'),
    path('api/user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    # Url for admin, ado and dda list paginated
    path('api/users-list/admin/', views.AdminViewSet.as_view({'get': 'list'}), name='admin-list'),
    path('api/users-list/dda/', views.DdaViewSet.as_view({'get': 'list'}), name='dda-list'),
    path('api/users-list/ado/', views.AdosViewSet.as_view({'get': 'list'}), name='ado-list'),

    path('api/upload/locations/', views.LocationList.as_view(), name='user-detail'),
    path('api/location/<int:pk>/', views.LocationDetail.as_view(), name='location-detail'),
    path('api/locations/<str:status>', views.LocationViewSet.as_view({'get': 'list'}), name='admin-location-list'),
    path('api/locations/ado/<str:status>', views.LocationViewSetAdo.as_view({'get': 'list'}), name='ado-location-list'),
    path('api/locations/dda/<str:status>', views.LocationViewSetDda.as_view({'get': 'list'}), name='dda-location-list'),
    path('api/admin/ado/<int:pk>/<str:status>', views.LocationViewSetAdoForAdmin.as_view({'get': 'list'}), name='admin-ado-location-list'),
    path('api/admin/dda/<int:pk>/<str:status>', views.LocationViewSetDdaForAdmin.as_view({'get': 'list'}), name='admin-dda-location-list'),
    # List of ados under a specific dda logged in
    path('api/ado/', views.AdoViewSet.as_view({'get': 'list'}), name='ado-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)