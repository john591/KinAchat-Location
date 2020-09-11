from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from django.contrib import messages

# Create your views here.
from .models import *
from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "ebay/loginPage.html", context)

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm()

    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            if next:
                return redirect(next)
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, "ebay/registerPage.html", context)

"""
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + ' votre compte a été créer')
            return redirect('login')

    context = {'form':form}
    return render(request, "ebay/registerPage.html", context)
"""
def logout_view(request):
    logout(request)
    return redirect('/')

def index(request):
    context = {
        "items": Article.objects.all()[:12],
        "categories": Categorie.objects.all(),
        "sous_categories":Sous_Categorie.objects.all()[:12],
        "sousimg": LienImage.objects.all()
    }
    return render(request, "ebay/index.html", context)

def apropos_view(request):
    return render(request, "ebay/apropos.html")


def sous_categorie_view(request, sous_cate_id):
    try:
        categorie = Categorie.objects.get(pk=sous_cate_id)
    except Categorie.DoesNotExist:
        raise Http404("Aucun sous categorie dans la base")
    context = {
        "categories": categorie,
        "sous_categories": categorie.groupe_categorie.all(),
        "sousimg": LienImage.objects.all()
    }
    return render(request, "ebay/sous_categorie.html", context)

def articles_view(request, article_id):
    try:
        sous_categories = Sous_Categorie.objects.get(pk=article_id)
    except Sous_Categorie.DoesNotExist:
        raise Http404("Aucune categorie dans la base")
    context = {
        "sous_categorie": sous_categories,
        "items": sous_categories.trieCat.all(),
        "img_l": LienImage.objects.all()
    }
    return render(request, "ebay/articles.html", context)

def achat_article(request, item_id):
    try:
        articles = Article.objects.get(pk=item_id)
    except Article.DoesNotExist:
        raise Http404("Cette article n'est plus disponible en stock, désolé!")
    context = {
        "article": articles,
        "tailles": Taille.objects.all(),
        "links": LienImage.objects.all()
    }
    return render(request, "ebay/achat_article.html", context)

"""
class CommandeDetail():
    model = Commande
    template_name = 'commandeDetails.html'
"""
