from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from . import models, forms
from django.core.paginator import Paginator
from django.urls import reverse



    

def search(request):
    
    form = forms.SearchForm(request.GET)

    if form.is_valid():
        category = form.cleaned_data.get("category")
        title = form.cleaned_data.get('title')

        filter_args = {}
        
        if category is not None:
            filter_args["category"] = category
        
        if title is not None:
            filter_args['title__contains']= title

        qs = models.Content.objects.filter(**filter_args).order_by('title')

        paginator = Paginator(qs, 5)

        page = request.GET.get("page", 1)
        

        posts = paginator.get_page(page)

        return render(request, "posts/faq_list.html", {"form": form, "posts": posts})


    else:
        form = forms.SearchForm()
    
    return render(request, "posts/faq_list.html", {"form": form})

class PostUpdateView(UpdateView):
    model = models.Content
    form_class = forms.UpdateForm
    template_name = 'posts/faq_update.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('posts:posts-admin-list')

class PostCreateView(CreateView):
    model = models.Content
    form_class = forms.UpdateForm
    template_name = 'posts/faq_update.html'

    def get_success_url(self):
        return reverse('posts:posts-admin-list')


class PostDeleteView(DeleteView):
    model = models.Content
    template_name = "posts/faq_delete.html"
    pk_url_kwarg = "pk"

    def get_success_url(self):
        return reverse('posts:posts-admin-list')

class PostAdminListView(ListView):
    model = models.Content
    template_name = 'core/adminpage_faq_list.html'
    context_object_name = 'posts'


