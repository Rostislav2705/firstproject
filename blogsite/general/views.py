from django.urls import reverse_lazy
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, authenticate, login
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def index(request):
    articles = Article.objects.all()
    query = request.GET.get('q')

    if query:
        articles = articles.filter(title__icontains=query)

    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/index.html', {'page_obj': page_obj, 'query': query})


def about(request):
    return render(request, 'main/about.html')

def post(request):
    return render(request, 'main/post.html')

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('article_detail', article_id=article.pk)
    else:
        form = CommentForm()

    return render(request, 'main/article_detail.html', {'article': article, 'form': form})




@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user  # Встановлюємо автора на поточного користувача
            article.save()
            return redirect('generalpage')
    else:
        form = ArticleForm()
    return render(request, 'main/article.html', {'form': form})


def login_view(request):
    context = {'form': CustomUserLoginForm}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(username, password, user)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('generalpage'))

    return render(request, template_name='main/login.html', context=context)


def sing_up(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = CustomUser.objects.create_user(username= username, email=email, password = password)
        print(user)
        return redirect(reverse_lazy('login'))
    return render(request, template_name='main/register.html', context={'form': CustomUserCreationForm})


def logout_view(request):
    logout(request)
    return redirect('generalpage')


def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        article.delete()
        return redirect('generalpage')

    return render(request)



def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', article_id=article_id)
    else:
        form = ArticleForm(instance=article)

    return render(request, 'main/edit_article.html', {'form': form})


