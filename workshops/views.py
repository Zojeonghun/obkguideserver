from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from . import models, forms
from django.urls import reverse
from django.core.paginator import Paginator

class WorkshopListView(ListView):
    model = models.Workshop
    template_name = 'workshops/workshop_list.html'
    context_object_name = 'workshops'

def search(request):

    form = forms.SearchForm(request.GET)

    if form.is_valid():
        location = form.cleaned_data.get("location")
        name = form.cleaned_data.get('name')
        address_text = form.cleaned_data.get('address_text')

        filter_args = {}
        
        if location is not None:
            filter_args["location"] = location
        
        if name is not None:
            filter_args['name__contains']= name

        if address_text is not None:
            
            filter_args['address_text__contains']= address_text
        qs = models.Workshop.objects.filter(**filter_args).order_by('?')

        paginator = Paginator(qs, 5)

        page = request.GET.get("page", 1)
        

        workshops = paginator.get_page(page)
        return render(request, "workshops/workshop_list.html", {"form": form, 'workshops':workshops })

    else:
        form = forms.SearchForm()
        

    return render(request, "workshops/workshop_list.html", {"form": form})

class WorkshopAdminDeleteView(DeleteView):
    model = models.Workshop
    template_name = "core/adminpageworkshop_delete.html"
    pk_url_kwarg = "pk"

    def get_success_url(self):
        return reverse('workshops:workshops-admin-list')

class WorkshopAdminCreateView(CreateView):
    models = models.Workshop
    form_class = forms.WorkshopAdminForm
    template_name = 'core/adminpageworkshop_update.html'

    def get_success_url(self):
        return reverse('workshops:workshops-admin-list')


class WorkshopAdminListView(ListView):
    model = models.Workshop
    template_name = 'core/adminpageworkshop_list.html'
    context_object_name = 'workshops'



class WorkshopAdminUpdateView(UpdateView):
    model = models.Workshop
    template_name = 'core/adminpageworkshop_update.html'
    context_object_name = 'workshop'
    form_class = forms.WorkshopAdminForm
    
    def get_success_url(self):
        return reverse('workshops:workshops-admin-list')


