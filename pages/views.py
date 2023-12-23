from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Page

# Create your views here.
class PageCreateView(CreateView):
    model = Page
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')

# Update View
class PageUpdateView(UpdateView):
    model = Page
    fields = ['title', 'content','order']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('pages:pages')
    
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id] ) + '?ok'

# Detail View
class PageDetailView(DetailView):
    model = Page


# List View
class PageListView(ListView):
    model = Page
    

class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
    
    

