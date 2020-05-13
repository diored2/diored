from django.contrib import admin
from django.urls import path, include
from routes.views import (home, find_routes, add_route,
                          RouteListView, RouteDetailView, RouteDeleteView)
from .views import login_view, logout_view, register_view

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('cities/', include(('cities.urls', 'city'))),
    path('trains/', include(('trains.urls', 'train'))),
    path('find/', find_routes, name='find_routes'),
    path('add_route/', add_route, name='add_route'),
    path('list/', RouteListView.as_view(), name='list'),
    path('detail/<int:pk>/', RouteDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', RouteDeleteView.as_view(), name='delete'),
    path('', home, name='home'),
]
