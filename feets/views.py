
from django.core import paginator
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse
from . import models, forms
from django.core.paginator import Paginator

# def Feet(request):
#     return render(request, 'feets/feets.html')

def FeetPage(request):
    return render(request, 'feets/feets.html')


def search(request):

    form = forms.SearchForm(request.GET)

    if form.is_valid():
        activity = form.cleaned_data.get("activity")
        hope = form.cleaned_data.get("hope")
        age = form.cleaned_data.get("age")
        waterproof = form.cleaned_data.get("waterproof")
        
        filter_args = {}
        
        if activity is not None:
            filter_args["activity"] = activity

        # for a in activity:
        #     filter_args["activity"] = a
        # if activity is not None:
        #     filter_args["activity"] = activity
        
        if hope is not None:
            filter_args["hope"] = hope

        if age is not None:
            filter_args["age"] = age

        if waterproof is not None:
            filter_args["waterproof"] = waterproof


        feets = models.Feet.objects.filter(**filter_args)


    else:
        form = forms.SearchForm()
        return render(request, "feets/search.html", {"form": form})


    return render(request, "feets/feets_list.html", {"form": form, "feets": feets})



def FeetListAllFilter(request):
    form = forms.FeetFilter(request.GET)
    if form.is_valid():
        function = form.cleaned_data.get("function")
        mobis_grade = form.cleaned_data.get("mobis_grade")
        rating = form.cleaned_data.get("rating")
        name = form.cleaned_data.get("name")

        filter_args = {}
        
        for a in function:
            filter_args["function"] = a
        # if function is not None:
        #     filter_args["function"] = function

        for m in mobis_grade:
            filter_args["mobis_grade"] = m

        for r in rating:
            filter_args["rating"] = r  

        if name is not None:
            filter_args['name__contains']= name       

        qs = models.Feet.objects.filter(**filter_args).order_by('id')

        paginator = Paginator(qs, 5)

        page = request.GET.get("page", 1)

        feets = paginator.get_page(page)


        return render(request, "feets/feets_list_all.html", {"form": form, "feets": feets})

    else:
        form = forms.FeetFilter(request.GET)

    return render(request, "feets/feets_list_all.html", {"form": form,})

    

class FeetDetailView(DetailView):
    model = models.Feet
    template_name = 'feets/feet_detail.html'
    context_object_name = 'feet'
    pk_url_kwarg = 'pk'


class FeetAdminListView(ListView):
    model = models.Feet
    template_name = 'core/adminpagefeet_list.html'
    context_object_name = 'feets'


class FeetAdminUpdateView(UpdateView):
    model = models.Feet
    template_name = 'core/adminpagefeet_update.html'
    context_object_name = 'feet'
    form_class = forms.FeetAdminForm

    def get_success_url(self):
        return reverse('feets:feets-admin-list')

class FeetDeleteView(DeleteView):
    model = models.Feet
    template_name = "posts/faq_delete.html"
    pk_url_kwarg = "pk"

    def get_success_url(self):
        return reverse('feets:feets-admin-list')