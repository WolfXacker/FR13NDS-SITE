from .models import Video
from django.shortcuts import render

# Create your views here.

def index(request):
    videos = Video.objects.all()
    return render(request, 'yotubevideo/youtube_video.html', context={'videos': videos})