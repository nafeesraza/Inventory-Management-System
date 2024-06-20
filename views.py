from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product, Order, StockTransfer

class ProductListView(ListView):
    model = Product
    template_name = 'inventory/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'inventory/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'inventory/product_form.html'
    fields = ['name', 'sku', 'description', 'price', 'quantity_in_stock']

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'inventory/product_form.html'
    fields = ['name', 'sku', 'description', 'price', 'quantity_in_stock']

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'inventory/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

# Similar implementations for Order and StockTransfer views
