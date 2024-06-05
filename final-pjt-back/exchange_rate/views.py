from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
# from .models import Exchange_rate
# from .serializers import ExchangeRateSerializer
import requests
from datetime import datetime, timedelta
from pytz import timezone
from django.conf import settings
EXCHANGE_API_KEY = settings.EXCHANGE_API_KEY
exchange_URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'

@api_view(['GET'])
def save_exchange_rate(request):
    today = datetime.now(timezone('Asia/Seoul'))
    now = today.strftime("%Y%m%d")

    if int(today.strftime("%H")) < 11:
        today -= timedelta(1)


    holiday = ['0501', '0506','0515', '0606', '0815', '0916', '0917', '0918', '1003', '1009', '1225']
    def find_working_day(today):
        global now
        while (True):
            # print(today, today.weekday())
            if today.weekday() < 5 and today.strftime('%m%d') not in holiday:
                now = today.strftime("%Y%m%d")
                return now
            today -= timedelta(1)

    now = find_working_day(today)
    params = {
        'authkey': EXCHANGE_API_KEY,
        'searchdate': now,
        'data': 'AP01'
    }
    response = requests.get(exchange_URL, params=params).json()
    # print(response)
    if not response or response[0].get('result') != 1: # 오류
        return Response('api error')
    for i in range(len(response)):
        response[i]['tts'] = response[i]['tts'].replace(',', "")
        if response[i].get('cur_unit') == 'KRW': # 한국
            response[i]['tts'] = '1'
            
        if "(100)" in response[i].get('cur_unit'):
            response[i]['cur_unit'] = response[i]['cur_unit'].replace("(100)", "")
            response[i]['tts'] = round(float(response[i]['tts'])/100, 2)
 
    return Response(response)


    # DB에 저장된 환율 정보를 가져오는 경우
    # rates = Exchange_rate.objects.all()
    # serializer = ExchangeRateSerializer(rates, many=True)
    # return Response(serializer.data)


# DB 생성 코드
# from django.conf import settings
# EXCHANGE_API_KEY = settings.EXCHANGE_API_KEY

# exchange_URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'

    

# @api_view(['GET'])
# def save_exchange_rate(request):
#     params = {
#         'authkey': EXCHANGE_API_KEY,
#         'searchdate': now,
#         'data': 'AP01'
#     }
#     response = requests.get(exchange_URL, params=params).json()
    
#     for cur in response:
#         if cur.get('result') != 1: # 오류
#             continue
 
#         save_data = {
#             'cur_unit': cur.get('cur_unit'),
#             'cur_nm': cur.get('cur_nm'),
#             'rate': float(cur.get('tts').replace(",","")),
#         }
#         if cur.get('cur_unit') == 'KRW': # 한국
#             save_data['rate'] = 1
            

#         if "(100)" in save_data.get('cur_unit'):
#             save_data['cur_unit'] = save_data['cur_unit'].replace("(100)", "")
#             save_data['rate'] = round(save_data['rate']/100, 2)

#         serializer = ExchangeRateSerializer(data=save_data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()

#     return JsonResponse({"m": '환율 저장완료'})
