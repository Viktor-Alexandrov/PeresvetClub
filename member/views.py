from django.shortcuts import render

def index(request):
    return render(request, 'member/index.html')

def coach(request):
    return render(request, 'member/coaching_staff.html')

def schedule(request):
    return render(request, 'member/training_schedule.html')

def news(request):
    return render(request, 'member/news.html')

def archive(request):
    return render(request, 'member/archive.html')
