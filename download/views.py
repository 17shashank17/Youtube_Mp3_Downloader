from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import youtube_dl
# Create your views here.
def index(request):
    if request.method=="POST":
        fetch_url=request.POST.get('fetch_url')
        print(fetch_url)
        ydl_opts = {
            'format': 'bestaudio/best',
            'download_archive': 'downloaded_songs.txt',
            'outtmpl': '%(title)s.mp3',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }],
        }
        ydl=youtube_dl.YoutubeDL(ydl_opts)
        with ydl:
            result = ydl.extract_info(
                fetch_url,
                download=False
            )

        if 'entries' in result:
            video = result['entries'][0]
        else:
            video = result
        url_embedded=video['formats'][0]['url']
    
        return HttpResponseRedirect(url_embedded)

    else:

        return render(request,'download/index.html')