from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_packages, name='category_packages'),
    path('package/<int:package_id>/', views.package_detail, name='package_detail'),
]