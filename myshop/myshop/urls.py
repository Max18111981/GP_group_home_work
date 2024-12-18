"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from store.views import product_list, category_products, cart_view, \
    add_to_cart, checkout, order_details, update_cart_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('', product_list, name='product_list'),
    path('category/<int:category_id>/', category_products, name='category_products'),
    path('cart/', cart_view, name='cart_view'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update-cart-item/<int:product_id>/', update_cart_item, name='update_cart_item'),
    path('checkout/', checkout, name='checkout'),
    path('order/<int:order_id>/', order_details, name='order_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
