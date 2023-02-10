from django.urls import path
from . import views


urlpatterns = [
    path("hello/", views.say_hello),
    ##### Products ####
    path("products/", views.productList),
    path("product/<str:pk>/", views.product),
    path("add-product/", views.addProduct),
    path("update-product/<str:pk>", views.updateProduct),
    path("delete-product/<str:pk>", views.deleteProduct),
    ### Vendors ####
    path("vendors/", views.vendorList),
    path("vendor/<str:pk>/", views.vendorOne),
    path("add-vendor/", views.addVendor),
    path("update-vendor/<str:pk>", views.updateVendor),
    path("delete-vendor/<str:pk>", views.deleteVendor),
    ### purchases ####
    path("purchases/", views.purchaseList),
    path("purchase/<str:pk>/", views.purchaseOne),
    path("add-purchase/", views.addPurchase),
    path("update-purchase/<str:pk>", views.updatePurchase),
    path("delete-purchase/<str:pk>", views.deletePurchase),
]
