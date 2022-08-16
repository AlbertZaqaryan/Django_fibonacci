from django.shortcuts import render
from .models import Fibonacci
# Create your views here.

def fibonacci(request):
    return render(request, 'fibonacci.html')


def fib(request):
    n = int(request.POST['n'])
    n1 = 0
    n2 = 1
    for i in range(2, n + 1):
        res = n1 + n2
        n1 = n2
        n2 = res
    return render(request, 'res.html', {'res':res})

def about(request):
    mylist = Fibonacci.objects.all()
    return render(request, 'about.html', {'mylist':mylist})