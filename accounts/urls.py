from django.urls import path
from . import views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "accounts"
urlpatterns = [
    path('',views.AccountCreateAPIView.as_view()),
    path('login/',TokenObtainPairView.as_view()),
]
