from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path('',views.ProductListAPIView.as_view()),
    path('<int:productId>/',views.ProductDetailListAPIView.as_view()),
]
