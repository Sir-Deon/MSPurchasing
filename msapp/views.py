from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer, VendorSerializer, PurchaseSerializer
from .models import Product, Vendor, Purchase

# Create your views here.


@api_view(["GET"])
def say_hello(request):
    return Response("Hello world !")


### Products API handlers #########
@api_view(["GET"])
def productList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def addProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["PUT"])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response("Deleted succesfully deleted  !!")


### Vendors API handlers #########
@api_view(["GET"])
def vendorList(request):
    vendors = Vendor.objects.all()
    serializer = VendorSerializer(vendors, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def vendorOne(request, pk):
    vendor = Vendor.objects.get(id=pk)
    serializer = VendorSerializer(vendor, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def addVendor(request):
    print(request.data)
    serializer = VendorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.error)


@api_view(["PUT"])
def updateVendor(request, pk):
    vendor = Vendor.objects.get(id=pk)
    serializer = VendorSerializer(instance=vendor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.error)


@api_view(["DELETE"])
def deleteVendor(request, pk):
    vendor = Vendor.objects.get(id=pk)
    vendor.delete()
    return Response("Deleted succesfully deleted  !!")


### Purchases API handlers #########
@api_view(["GET"])
def purchaseList(request):
    purchases = Purchase.objects.all()
    serializer = PurchaseSerializer(purchases, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def purchaseOne(request, pk):
    purchase = Purchase.objects.get(id=pk)
    serializer = PurchaseSerializer(purchase, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def addPurchase(request):
    print(request.data)
    serializer = PurchaseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.error)


@api_view(["PUT"])
def updatePurchase(request, pk):
    purchase = Purchase.objects.get(id=pk)
    serializer = PurchaseSerializer(instance=purchase, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def deletePurchase(request, pk):
    purchase = Purchase.objects.get(id=pk)
    purchase.delete()
    return Response("Deleted succesfully deleted  !!")
