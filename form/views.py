from django.shortcuts import render, redirect, get_object_or_404
from .form import CustomerForm
from .models import Customer,Room
from django.views.generic import ListView, DetailView, TemplateView
# Create your views here.

class Home(TemplateView):
    template_name = 'form/home.html'

def form_new(request):
    if request.method == "POST":
        form =CustomerForm(request.POST)
        if form.is_valid():
            customer=form.save(commit=False)
            customer.save()
            return redirect('form_detail', pk=customer.pk)
    else:
        form = CustomerForm()
    return render(request, 'form/form_new.html', {'form': form})


class Details(DetailView):
    model = Customer
    template_name = 'form/customer_detail.html'

def form_edit(request, pk):
    post = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('form_detail', pk=post.pk)
    else:
        form = CustomerForm(instance=post)
    return render(request, 'form/form_new.html', {'form': form})

class Customers_list(ListView):
     template_name = 'form/customer_list.html'
     context_object_name = 'customer_list'
     def get_queryset(self):
         return Customer.objects.filter(checkout=False)

class Room_list(ListView):
    template_name = "form/room_list.html"
    context_object_name = "room_list"
    def get_queryset(self):
        return Room.objects.all()

class Room_details(DetailView):
    model = Room
    template_name = "form/room_detail.html"
    context_object_name = "customer"

    # def get_queryset(self):
    #     room_use = Room.objects.get(pk=self.kwargs['pk'])
    #     room_use = room_use.customer_set.all()
    #     print(room_use)
    #     return room_use

    def get_object(self, queryset=None):
        obj = get_object_or_404(self.model, room_number=self.kwargs['number'])
        print(obj)
        return obj

    def get_context_data(self, **kwargs):
        room = super().get_context_data()
        room['members'] = room['customer'].customer_set.all()
        print(room)
        return room
        # return room.customer_set.all()



def checkout(request):
    customer= Customer.objects.get(checkout=True)
