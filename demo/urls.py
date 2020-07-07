from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import store.views
import store.api_views

urlpatterns = [
	path('api/products/', store.api_views.ProductList.as_view(), name='productlist'),
	path('api/products/new/', store.api_views.ProductCreation.as_view(), name='productcreate'),
	path('api/products/delete/<int:id>/', store.api_views.ProductDestroy.as_view(), name= 'productdestroy'),
	path('api/products/<int:id>/update/', store.api_views.ProductUpdate.as_view()),
	path('api/products/<int:id>/', store.api_views.ProductRetrieve.as_view(),name='productretrieve'),
	path('api/products/updatedestroyretrieve/<int:id>/', store.api_views.ProductRetrieveUpdateDestroy.as_view(), name='ProductRetrieveUpdateDestroy'),
	path('api/products/<int:id>/stats/', store.api_views.ProductStats.as_view()),

    path('admin/', admin.site.urls),
    path('products/<int:id>/', store.views.show, name='show-product'),
    path('cart/', store.views.cart, name='shopping-cart'),
    path('', store.views.index, name='list-products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
