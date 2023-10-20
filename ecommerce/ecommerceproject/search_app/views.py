from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
from django.http import HttpResponse  # Import HttpResponse

def searchResult(request):
    products = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request, 'search.html', {'query': query, 'products': products})
    else:
        no_query_message = "No search query provided."
    return HttpResponse(no_query_message)

