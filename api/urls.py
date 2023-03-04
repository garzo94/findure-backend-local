from django.urls import path, include
from .views import SignUpView, LoginView, ProductViewSet, CategoryViewSet, UserView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/data/', UserView.as_view(), name='users-data'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
]