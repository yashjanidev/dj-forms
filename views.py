from django.shortcuts import render, redirect
from .models import EventInfo
from .forms import EventFormdata
# Create your views here.

def card_page(request):
    data = EventInfo.objects.all()
    return render(request, 'stem_app/card_page.html', {'data': data})

def form_page(request):
    if request.method == 'POST':
        form = EventFormdata(request.POST)
        if form.is_valid():
            form.save()
            return redirect('card_page')
    else:
        form = EventFormdata()
    return render(request, 'stem_app/form_page.html', {'form': form})
