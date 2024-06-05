from django.db import models
from accounts.models import User

class Products(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융 상품코드
    dcls_month = models.TextField() # 공시 제출월
    fin_prdt_nm = models.TextField() # 금융 상품명
    kor_co_nm = models.TextField() # 금융 회사명
    spcl_cnd = models.TextField() # 우대조건
    prdt_type = models.TextField() # 예/적금
    

class Options(models.Model):
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField() # 금융 상품코드
    intr_rate_type_nm = models.CharField(max_length=100) # 저축금리 유형명
    save_trm = models.TextField() # 저축기간(월단위)
    intr_rate = models.FloatField() # 저축금리
    intr_rate2 = models.FloatField() # 최대우대금리


class JoinList(models.Model):
  option_id = models.TextField()
  product_id = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)