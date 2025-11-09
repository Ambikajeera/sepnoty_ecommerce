# from rest_framework import viewsets, permissions
# from .models import Product, Order
# from .serializers import ProductSerializer, OrderSerializer

# class IsAdminUser(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user and request.user.is_staff

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [permissions.IsAuthenticated, IsAdminUser]

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [permissions.IsAuthenticated, IsAdminUser]

#     # Optional: update status
#     def update(self, request, *args, **kwargs):
#         order = self.get_object()
#         order.status = request.data.get('status', order.status)
#         order.admin_notes = request.data.get('admin_notes', order.admin_notes)
#         order.save()
#         return super().retrieve(request, *args, **kwargs)

from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})
