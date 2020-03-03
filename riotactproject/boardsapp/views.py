from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from boardsapp.models import Board


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', { 'boards': boards })