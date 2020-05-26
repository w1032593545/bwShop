# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from goods.serializers import GoodsSerializer,CategorySerializer
from .models import Goods,GoodsCategory
from .filters import GoodsFilter

# 自定义分页
from rest_framework.pagination import PageNumberPagination

class GoodsPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 12
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 100
# class GoodsListView(APIView):
#     def get(self,request,format=None):
#         goods = Goods.objects.all()
#         goods_serializer = GoodsSerializer(goods,many=True)
#         return Response(goods_serializer.data)

# class GoodsListView(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer

# class GoodsListView(generics.ListAPIView):
#     pagination_class = GoodsPagination
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer

class GoodsListViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''
        list:
            商品列表，分页，搜索，过滤，排序
        retrieve:
            获取商品详情
    '''
    pagination_class = GoodsPagination
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    # 设置筛选
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class = GoodsFilter

    # 设置搜索
    search_fields = ('name','goods_brief','goods_desc')
    # 排序
    ordering_fields = ("sold_num","shop_price")


class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer