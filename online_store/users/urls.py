from django.urls import path
from .views import RegisterView, UserLoginView, UserLogoutView, UserProfileView, UserUpdateView, \
    ChangePasswordViewDone, ChangePasswordView, HistoryOrderList, HistoryDetailOrder
from rest_framework import routers
from .api import UserViewSet

router = routers.DefaultRouter()
router.register('api/users', UserViewSet)

# urlpatterns = router.urls

urlpatterns = [
    path('registration/', RegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='account'),
    path('profile/historyorder/', HistoryOrderList.as_view(), name='history_order'),
    path('profile/oneorder/<int:pk>/', HistoryDetailOrder.as_view(), name='one_order'),
    path('profile/update/', UserUpdateView.as_view(), name='update_profile'),
    path('profile/password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('profile/password-change/done/', ChangePasswordViewDone.as_view(), name='password_change_done'),
] + router.urls
