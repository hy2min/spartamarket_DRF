from django.urls import path
from . import views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
)

app_name = "accounts"
urlpatterns = [
    path('',views.AccountCreateAPIView.as_view()),
    path('login/',TokenObtainPairView.as_view()),
    path('<str:username>/',views.AccountDetailAPIView.as_view()),
    ]
