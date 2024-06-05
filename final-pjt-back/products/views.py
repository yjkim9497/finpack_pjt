from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Products, Options, JoinList
from .serializers import ProductsSerializer, OptionsSerializer, JoinListSerializer, JoinSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404

@api_view(['GET'])
def product_list(request):
    products = Products.objects.all()
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def option_list(request, pk):
    prdt = Products.objects.get(pk=pk)
    options = prdt.options_set.all()
    serializer = OptionsSerializer(options, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def all_option_list(request):
    options = Options.objects.all()
    serializer = OptionsSerializer(options, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def join_list(request):
    if request.method == 'GET':
        user = request.user

        join_list = get_list_or_404(JoinList.objects.filter(user=user))
        print(join_list)
        serializer = JoinListSerializer(join_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = JoinSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# DB 생성 코드
# from django.conf import settings
# PRDT_API_KEY = settings.PRDT_API_KEY
# deposit_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'

# @api_view(['GET'])
# def save_deposit_products(request):
#     params = {
#         'auth': PRDT_API_KEY,
#         'topFinGrpNo': '020000', 
#         'pageNo': 1
#     }
#     response = requests.get(deposit_URL, params=params).json()
    
#     for prdt in response.get('result').get('baseList'):
#         save_data = {
#             'fin_prdt_cd': prdt.get('fin_prdt_cd'),
#             'dcls_month': prdt.get('dcls_month'),
#             'fin_prdt_nm': prdt.get('fin_prdt_nm'),
#             'kor_co_nm': prdt.get('kor_co_nm'),
#             'spcl_cnd': prdt.get('spcl_cnd'),
#             'prdt_type': 'deposit',
#         }
#         serializer = ProductsSerializer(data=save_data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()

#     for prdt in response.get('result').get('optionList'):
#         fin_prdt_cd = prdt.get('fin_prdt_cd')
#         save_data = {
#             'fin_prdt_cd' : prdt.get('fin_prdt_cd'),
#             'intr_rate_type_nm' : prdt.get('intr_rate_type_nm'),
#             'save_trm' : prdt.get('save_trm'),
#             'intr_rate' : prdt.get('intr_rate'),
#             'intr_rate2' : prdt.get('intr_rate2', -1),
#         }
#         serializer = OptionsSerializer(data=save_data)
#         if serializer.is_valid(raise_exception=True):
#             if Products.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
#                 product = Products.objects.get(fin_prdt_cd=fin_prdt_cd)
#                 serializer.save(product=product)

#     return JsonResponse({"m": '예금 저장완료'})

# saving_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

# @api_view(['GET'])
# def save_saving_products(request):
#     params = {
#         'auth': PRDT_API_KEY,
#         'topFinGrpNo': '020000', 
#         'pageNo': 1
#     }
#     response = requests.get(saving_URL, params=params).json()
    
#     for prdt in response.get('result').get('baseList'):
#         save_data = {
#             'fin_prdt_cd': prdt.get('fin_prdt_cd'),
#             'dcls_month': prdt.get('dcls_month'),
#             'fin_prdt_nm': prdt.get('fin_prdt_nm'),
#             'kor_co_nm': prdt.get('kor_co_nm'),
#             'spcl_cnd': prdt.get('spcl_cnd'),
#             'prdt_type': 'saving',
#         }
#         serializer = ProductsSerializer(data=save_data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()

#     for prdt in response.get('result').get('optionList'):
#         fin_prdt_cd = prdt.get('fin_prdt_cd')
#         save_data = {
#             'fin_prdt_cd' : prdt.get('fin_prdt_cd'),
#             'intr_rate_type_nm' : prdt.get('intr_rate_type_nm'),
#             'save_trm' : prdt.get('save_trm'),
#             'intr_rate' : prdt.get('intr_rate'),
#             'intr_rate2' : prdt.get('intr_rate2', -1),
#         }
#         serializer = OptionsSerializer(data=save_data)
#         if serializer.is_valid(raise_exception=True):
#             if Products.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
#                 product = Products.objects.get(fin_prdt_cd=fin_prdt_cd)
#                 serializer.save(product=product)

#     return JsonResponse({"m": '적금 저장완료'})