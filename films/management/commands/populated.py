from django.core.management.base import BaseCommand
from films.models import Video

class Command(BaseCommand):
    help = 'Populate videos in the database'

    def handle(self, *args, **options):
        url_links = [
            "/static/videos/hahaha.mp4",
            "https://www.youtube.com/embed/XhW_ZsFZZIk",
            "https://www.youtube.com/embed/mQmFbcFZFhQ",
            "https://www.youtube.com/embed/TAMyLwW9HW8",
            "https://www.youtube.com/embed/zkI0LRK-vEU",
            "https://www.youtube.com/embed/pM3CFiZOU4k",
            "https://www.youtube.com/embed/sEJKG60a1Zc",
            "https://www.youtube.com/embed/YnkgjKI3tR0",
            "https://www.youtube.com/embed/ph2Yw7yeeCw",
            "/static/videos/hahaha.mp4",
            "https://www.youtube.com/embed/7xnz43e0ahA",
            "/static/videos/hahaha.mp4",
            "/static/videos/hahaha.mp4",
            "/static/videos/hahaha.mp4",
            "/static/videos/hahaha.mp4",
            "/static/videos/hahaha.mp4",
            "/static/videos/hahaha.mp4",
            "/static/videos/hahaha.mp4",
            "/static/videos/hahaha.mp4",
            "/static/videos/hahaha.mp4",
            "/static/videos/hahaha.mp4",
            "/static/videos/hahaha.mp4",
            "https://www.youtube.com/embed/Xg3FFi2hLyY&t=2s",
            # Add more URLs as needed
        ]

        for index, url in enumerate(url_links, start=0):
            Video.objects.create(title=f'Video {index}', url=url)

        self.stdout.write(self.style.SUCCESS('Videos populated successfully.'))