from django.shortcuts import render
from django.shortcuts import render
# from blog.models import Article
from account.forms import NewsletterForm
from .models import NewsLetter, Presentation, Trouver_le_velo, Our_products, Feeback,News,Pub,Category_product
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    presentation = Presentation.objects.filter()[:1]
    velo = Trouver_le_velo.objects.filter()[:1]
    our_products = Our_products.objects.all()
    product = Category_product.objects.filter()[:1]
    feeback = Feeback.objects.all()
    top = Our_products.objects.all()
    news = News.objects.all()
    pub = Pub.objects.all()




    n_form = NewsletterForm()
    
    if request.method == 'POST':
        email = request.POST.get('email')
        n_form = NewsletterForm(request.POST)
        
        
        if n_form.is_valid():
            n_form.save()
            return HttpResponseRedirect(request.path_info)

        else:
            messages.warning(request, 'veuillez entrer ue addresse email valide svp')
        
    datas= {
        'n_form': n_form,
        'presentation':presentation,
        'velo':velo,
        'product':product,
        'news':news,
        'pub':pub,
        'top':top,
        'our_products':our_products,
        'feeback':feeback,
        

    }
    return render(request, 'website/index.html', datas)

def contacts(request):
    n_form = NewsletterForm()
    
    if request.method == 'POST':
        email = request.POST.get('email')
        n_form = NewsletterForm(request.POST)
        
        
        if n_form.is_valid():
            n_form.save()
            return HttpResponseRedirect(request.path_info)
        else:
            messages.warning(request, 'veuillez entrer ue addresse email valide svp')
    
    datas= {
        'n_form': n_form,
    }
    return render(request, 'website/contacts.html', datas)


def about(request):
    return render(request, 'website/about.html')






