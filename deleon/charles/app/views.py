from django.views import View
from django.shortcuts import render
from django.urls import reverse



class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/home.html', {'title': 'Home'})


class AboutPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/about.html', {'title': 'About Us'})


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Role

class RoleListView(ListView):
    model = Role
    template_name = 'app/role_list.html'

class RoleDetailView(DetailView):
    model = Role
    template_name = 'app/role_detail.html'

class RoleCreateView(CreateView):
    model = Role
    template_name = 'app/role_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('role_list')

class RoleUpdateView(UpdateView):
    model = Role
    template_name = 'app/role_form.html'
    fields = ['name', 'description']
    
    def get_success_url(self):
        return reverse('role_list')
class RoleDeleteView(DeleteView):
    model = Role
    template_name = 'app/role_confirm_delete.html'
    success_url = reverse_lazy('role_list')
