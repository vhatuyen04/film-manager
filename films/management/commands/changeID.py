from django.core.management.base import BaseCommand
from films.models import Video

class Command(BaseCommand):
    help = 'Update video IDs'

    def handle(self, *args, **kwargs):
        videos = Video.objects.all()
        current_id = 1

        for video in videos:
            video.id = current_id
            video.save()
            current_id += 1
            print(video.id)
            print('\n')
            print(video.title)
            print('\n')
        
        self.stdout.write(self.style.SUCCESS('Videos updated ID successfully.'))