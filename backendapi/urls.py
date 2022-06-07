from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('',views.apioverview,name='home'),
    path('plan-api',views.fetchplan,name='plan-api'),
    path('plan-update/<str:pk>/', views.planUpdate, name="plan-update"),
    path('info-api',views.Get_Info,name='info-api'),
    path('sumbit-info',views.sumbit_info,name='sumbit-info'),
    path('admin-auth',views.admin_auth_login,name='admin-auth'),
    path('new-plan',views.new_plan,name='new-plan'),
    path('create-admin',views.create_admin_user,name='create-admin'),
    path('user-signup',views.user_signup,name='user-signup'),
    path('sysadmin',views.sumbit_ticket,name='sysadmin'),
    path('fetch-ticket/<str:pk>/',views.fetch_ticket,name='fetch-ticket'),
    path('place-order',views.place_order,name='place-order'),
    path('get-order/<str:pk>/',views.get_order,name='get-order'),
    
    # path for tokens
    path('api/api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
]
