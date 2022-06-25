from django.urls import path

from assets import views

urlpatterns = [
    path('assets/', views.AssetList.as_view(), name='asset-list'),
    path('assets/<slug:pk>/', views.AssetDetail.as_view(), name='asset-detail'),
]
