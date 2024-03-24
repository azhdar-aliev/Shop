from django.urls import path, include

from .views import index_view, product_list_view

urlpatterns = [
    path('', index_view),
    path('category/', product_list_view, name='product_list'),
    path('category/<slug:category_slug>', product_list_view, name='product_list_by_category')
]
