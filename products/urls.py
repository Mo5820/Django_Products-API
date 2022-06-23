from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
app_name='products'
urlpatterns = [
    path('',views.ProductListView.as_view(),name='ApiList'),
    path('<int:pk>/',views.ProductDetailView.as_view(),name='ApiDetail'),
    path('create',views.CreateProductiew.as_view(),name='Create'),
    path('destory/<int:pk>/',views.DestoryProductView.as_view(),name='DestoryView'),
    path('',views.List_Api,name='ListApi'),
    path('<int:pk>/',views.List_Api,name='ListApi'),
    path('',views.ProductMixinsView.as_view()),
    path('<int:pk>/',views.ProductMixinsView.as_view()),
    path('auth/',obtain_auth_token),
]
