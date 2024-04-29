from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProductListAPIView.as_view()),
    path('/<int:productID>/',views.ProductDetailListAPIView.as_view()),
]
