from distutils.log import error
from urllib import response
from django.shortcuts import render
from requests import Response
from rest_framework import generics,mixins,permissions,authentication
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
class ProductListView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # lookup_field='pk'

class CreateProductiew(generics.CreateAPIView):
    serializer_class=ProductSerializer

class DestoryProductView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
@api_view(["GET","POST"])
def List_Api(request,pk=None):
    method=request.method
    if method=="GET":
        if pk is not None:
            obj=get_object_or_404(Product,pk=pk)
            data=ProductSerializer(obj,many=False).data
            return Response(data)
 
        
        queryset=Product.objects.all()
        data=ProductSerializer(queryset,many=True).data
        return Response(data)


    if method=="POST":
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            title=serializer.validated_data.get("title")
            content=serializer.validated_data.get("content")or None
            if content is None:
                content=title
            serializer.save(content=content)
            return Response(serializer.data)

class ProductMixinsView(mixins.ListModelMixin,
mixins.RetrieveModelMixin,
mixins.CreateModelMixin,
generics.GenericAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    authentication_classes=[authentication.SessionAuthentication]
    def get(self,request,*args,**kwargs):
        pk=kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self,serializer):
        title=serializer.validated_data.get("title")
        content=serializer.validated_data.get("content") or None
        if content is None:
            content=title
        serializer.save(content=content)


    
    

