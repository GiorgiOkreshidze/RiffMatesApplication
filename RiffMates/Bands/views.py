from django.shortcuts import render, get_object_or_404
from .models import Musician, Band, Venue
from django.core.paginator import Paginator

# Create your views here.
def musician(request, id):
    musician = get_object_or_404(Musician, id = id)

    data = {
        "musician": musician
    }

    return render(request, "bands/musician.html", data)

def musicians(request):
    all_musicians = Musician.objects.all().order_by('last_name')

    number_of_objects_per_page = objects_per_page(request, all_musicians)

    paginator = Paginator(all_musicians, number_of_objects_per_page)

    page_num = get_page_num(request, paginator)

    page = paginator.page(page_num)

    data = {
        'musicians': page.object_list,
        'page': page
    }

    return render(request, 'bands/musicians.html', data)

def band(request, id):
    band = get_object_or_404(Band, id = id)

    data = {
        'band': band
    }

    return render(request, 'bands/band.html', data)

def bands(request):
    bands = Band.objects.all().order_by('name')
    number_of_objects_per_page = objects_per_page(request, bands)

    paginator = Paginator(bands, number_of_objects_per_page)

    page_num = get_page_num(request, paginator)

    page = paginator.page(page_num)

    data = {
        'bands': page.object_list,
        'page': page
    }

    return render(request, 'bands/bands.html', data)

def venues(request):
    venues = Venue.objects.all()
    number_of_objects_per_page = objects_per_page(request, venues)

    paginator = Paginator(venues, number_of_objects_per_page)

    page_num = get_page_num(request, paginator)

    page = paginator.page(page_num)

    data = {
        'venues': page.object_list,
        'page': page
    }

    return render(request, 'bands/venues.html', data)


def objects_per_page(request, objects):
    number_of_objects_per_page = request.GET.get('per_page', 1)
    number_of_objects_per_page = int(number_of_objects_per_page)

    if number_of_objects_per_page < 1:
        number_of_objects_per_page = 1
    elif number_of_objects_per_page > objects.count():
        number_of_objects_per_page = objects.count()

    return number_of_objects_per_page

def get_page_num(request, paginator):
    page_num = request.GET.get('page', 1 )
    page_num = int(page_num)

    if page_num < 1:
        page_num = 1
    elif page_num > paginator.num_pages:
        page_num = paginator.num_pages

    return page_num

