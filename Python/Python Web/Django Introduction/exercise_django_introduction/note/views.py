from http.client import responses

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from note.models import Note, Category


# Create your views here.
def home(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'home.html', context)

def search(request):
    name = request.GET.get('search')
    notes = Note.objects.filter(title__icontains=name) if name else Note.objects.all()
    response =list()
    for note in notes:
        response.append({'id': note.id, 'title': note.title, 'body': note.body, 'categories': [note[1] for note in note.category.values_list()]})


    return JsonResponse({'notes': response})


