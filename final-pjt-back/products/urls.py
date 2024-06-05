from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.product_list),
    path('options/', views.all_option_list),
    path('products/<int:pk>/', views.option_list),
    path('join/',views.join_list),


    # DB 생성 코드
    # path('product/save-deposit-products/', views.save_deposit_products),
    # path('product/save-saving-products/', views.save_saving_products),
]
