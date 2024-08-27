from django.urls import path
from .views import (
    CategoryListView, CategoryDetailView, ProductDetailView,
    AdminCategoryListView, AdminCategoryDetailView,
    AdminBrandListView, AdminBrandDetailView,
    AdminProductListView, AdminProductDetailView
)

urlpatterns = [
    # Public endpoints
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # Admin endpoints
    path('admin/categories/', AdminCategoryListView.as_view(), name='admin-category-list'),
    path('admin/categories/<int:pk>/', AdminCategoryDetailView.as_view(), name='admin-category-detail'),
    path('admin/brands/', AdminBrandListView.as_view(), name='admin-brand-list'),
    path('admin/brands/<int:pk>/', AdminBrandDetailView.as_view(), name='admin-brand-detail'),
    path('admin/products/', AdminProductListView.as_view(), name='admin-product-list'),
    path('admin/products/<int:pk>/', AdminProductDetailView.as_view(), name='admin-product-detail'),
]
