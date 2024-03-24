from django.urls import path, include

from .views import index_view, product_list_view, product_detail_view

app_name = 'shop_app'

urlpatterns = [
    path('', index_view),
    path('category/', product_list_view, name='product_list'),
    path('category/<slug:category_slug>', product_list_view, name='product_list_by_category'),
    path('product/<slug:slug>', product_detail_view, name='product_detail'),
]
