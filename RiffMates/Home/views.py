from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import date, timedelta


# Create your views here.
def credits(request):
    return HttpResponse("Credits Page", content_type="text/plain")

def about(request):
    return HttpResponse("<h1>About Page</h1>", content_type="text/html")

def version(request):
    return JsonResponse({"version" : "1.0"})

def news(request):
    today = date.today()
    before1 = today - timedelta(days=1)
    before2 = today - timedelta(days=2)

    data = {
        'news': [
            (today, "Advanced news added! Even more exclamation points!!!"),
            (before1, "RiffMates now has a news page!"),
            (before2, "RiffMates has its first web page"),
        ],
    }
    return render(request, 'home/news.html', data)