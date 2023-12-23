from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .models import Page

# Create your views here.

# Detail View
class PageDetailView(DetailView):
    model = Page
    
    
# def page(request, page_id, page_slug):
#     page = get_object_or_404(Page, id=page_id)
#     return render(request, 'pages/page.html', {'page':page})


# List View
class PageListView(ListView):
    model = Page
    
# def pages(request):
#     pages = get_list_or_404(Page)
#     return render(request, 'pages/pages.html', {'pages':pages})

