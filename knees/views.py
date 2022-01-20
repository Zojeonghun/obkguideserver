from django.core import paginator
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render
from django.urls import reverse
from . import models, forms
from django.core.paginator import Paginator

def Knees(request):
    return render(request, 'knees/knees.html')


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


        knees = models.Knee.objects.filter(**filter_args)


    else:
        form = forms.SearchForm()
        return render(request, "knees/search.html", {"form": form})


    return render(request, "knees/knees_list.html", {"form": form, "knees": knees})


def KneeListAllFilter(request):
    form = forms.KneeFilter(request.GET)
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

        qs = models.Knee.objects.filter(**filter_args).order_by('id')

        paginator = Paginator(qs, 5)

        page = request.GET.get("page", 1)

        knees = paginator.get_page(page)


        return render(request, "knees/knees_list_all.html", {"form": form, "knees": knees})

    else:
        form = forms.KneeFilter(request.GET)

    return render(request, "knees/knees_list_all.html", {"form": form,})

class KneeDetailView(DetailView):
    model = models.Knee
    template_name = 'knees/knee_detail.html'
    context_object_name = 'knee'
    pk_url_kwarg = 'pk'

class KneeAdminListView(ListView):
    model = models.Knee
    template_name = 'core/adminpageknee_list.html'
    context_object_name = 'knees'


class KneeAdminUpdateView(UpdateView):
    model = models.Knee
    template_name = 'core/adminpageknee_update.html'
    context_object_name = 'knee'
    form_class = forms.KneeAdminForm

    def get_success_url(self):
        return reverse('knees:knees-admin-list')


class KneeAdminCreateView(CreateView):
    models = models.Knee
    form_class = forms.KneeAdminForm
    template_name = 'core/adminpageknee_update.html'

    def get_success_url(self):
        return reverse('knees:knees-admin-list')

class KneeDeleteView(DeleteView):
    model = models.Knee
    template_name = "posts/faq_delete.html"
    pk_url_kwarg = "pk"

    def get_success_url(self):
        return reverse('knees:knees-admin-list')