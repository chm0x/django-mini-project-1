from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm



# Create your views here.
@method_decorator(staff_member_required, name='dispatch')
class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')
    
    

# Update View
@method_decorator(staff_member_required, name='dispatch')

class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'
    
    # success_url = reverse_lazy('pages:pages')
    
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id] ) + '?ok'

# Detail View
class PageDetailView(DetailView):
    model = Page


# List View
class PageListView(ListView):
    model = Page
    
@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
    
    

