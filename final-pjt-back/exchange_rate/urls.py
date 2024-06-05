from django.urls import path
from . import views


urlpatterns = [
    path('exchange/', views.save_exchange_rate),
    # DB 생성 코드
    # path('save-exchange-rate/', views.save_exchange_rate),
]
