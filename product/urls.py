from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),
    path('product/products', views.product_display, name='product'),
    path('product/add_product', views.add_product, name='add_product'),
    path('product/<int:id>/product_detail', views.product_detail, name='product_detail'),
    path('product/<int:id>/carousel_img', views.get_carousel_images, name='carousel')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)