from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



posts = [
    {
        'author': '30 steph curry',
        'title': 'town',
        'content': 'San fransisco , california',
        'date_posted': ' 31/01/2020'
    },
    {
        'author': '11 klay Thompson',
        'title': 'warriors nation',
        'content': 'oaklande , california',
        'date_posted': '01/02/2020'
    },
    {
        'author': '35 kevin durant',
        'title': 'brooklyn ',
        'content': ' New york city',
        'date_posted': '01/02/2020'
    },
    {
        'author': '1 Devin booker',
        'title': 'pheonix suns',
        'content': 'Arizona',
        'date_posted': '01/02/2020'
    },
    {
        'author': '13 James harden',
        'title': 'Houston rocket',
        'content': 'Houston',
        'date_posted': '01/02/2020'
    }

]


def home(request) :
	context = {
	       'posts' : Post.objects.all()
	}
	return render(request, 'base/home.html' , content )                #  HttpResponse('<h> INPT_NETwORK </h1>')



class PostListView(ListView):
    model = Post
    template_name = 'base/home.html'
    context_object_name = 'posts'    
    ordering = '-date_posted'


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post   
    fields = ['title','content'] 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def apropos(request) :
	return render(request, 'base/apropos.html' , {'title':'apropos page 1 test'})

