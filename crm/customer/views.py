from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse_lazy
from django.views.generic import (
    ListView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Customer
from .forms import CustomerForm, CustomerDeleteForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.
class CustomerListView(ListView):
    template_name = "customer/customer_list.html"
    model = Customer
    paginate_by = 10
    

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            object_list = self.model.objects.filter(
                Q(first_name__contains=name) | Q(last_name__contains=name)
            )
        else:
            object_list =  self.model.objects.all()
        return object_list
    

class CustomerCreateView(CreateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm
    success_url = reverse_lazy("customer:customer-list")

    def form_valid(self, form):
        return super().form_valid(form)

class CustomerUpdateView(UpdateView):        
    template_name = "customer/customer.html"
    form_class = CustomerForm
    success_url = reverse_lazy("customer:customer-list")

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)

    def form_valid(self, form):
        return super().form_valid(form)

class CustomerDeleteView(DeleteView):        
    model = Customer
    success_url = reverse_lazy("customer:customer-list")

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)


