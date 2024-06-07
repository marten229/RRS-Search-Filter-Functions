from django.shortcuts import render
from SearchFilterFunctions.models import Restaurant, Cuisine
from django.db.models import Q

def search_restaurants(request):
    query = request.GET.get('q')
    cuisines = request.GET.getlist('cuisines')

    filters = Q()
    
    if query:
        filters &= Q(name__icontains=query) | Q(description__icontains=query) | Q(address__icontains=query)
    
    if cuisines:
        filters &= Q(cuisines__id__in=cuisines)

    results = Restaurant.objects.filter(filters).distinct()
    
    all_cuisines = Cuisine.objects.all()
    
    return render(request, 'SearchFilterFunctions/search_results.html', {
        'results': results,
        'all_cuisines': all_cuisines,
        'selected_cuisines': cuisines,
        'query': query,
    })