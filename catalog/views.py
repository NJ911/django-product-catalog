from django.shortcuts import render

# Create your views here.
from .models import Category, Tag, Product

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    #Reading the inputs from database
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', '')
    selected_tag = request.GET.get('tag', '')

    if query:
        products = products.filter(description__icontains=query)  #filtering the products based on the query
    if category_id:
        products = products.filter(category_id=category_id)  #filtering the products based on the category
    if selected_tag:
        products = products.filter(tags__id=selected_tag)  #filtering the products based on the tag

    context = {
        'products': products,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'catalog/product_list.html', context)  #rendering the product list page with the context