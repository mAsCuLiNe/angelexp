from django.shortcuts import get_object_or_404, render


def consent(request):
    return render(request, 'main/consent.html')

def thanks(request):
    return render(request, 'main/thanks.html')
