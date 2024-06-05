from django.shortcuts import render
from SearchFilterFunctions.models import Restaurant
from django.db.models import Q

def search_restaurants(request):
    query = request.GET.get('q', '')
    city = request.GET.get('city', '')
    cuisine = request.GET.get('cuisine', '')
    available = request.GET.get('available', '')

    restaurants = Restaurant.objects.all()

    if query:
        restaurants = restaurants.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    if city:
        restaurants = restaurants.filter(city__iexact=city)

    if cuisine:
        restaurants = restaurants.filter(cuisine__iexact=cuisine)

    if available:
        restaurants = restaurants.filter(available=(available.lower() == 'true'))

    context = {
        'restaurants': restaurants,
        'query': query,
        'city': city,
        'cuisine': cuisine,
        'available': available,
    }

    return render(request, 'SearchFilterFunctions/search_results.html', context)
