from django.core.management.base import BaseCommand
from films.models import Video

class Command(BaseCommand):
    help = 'Update video IDs'

    def handle(self, *args, **kwargs):
        videos = Video.objects.all()

        # Update the link for each video object
        for video in videos:
            if video.url.startswith('static/'):
                # Replace 'static/' with '/static/'
                video.url = '/' + video.url

            # Save the updated video object back to the database
            video.save()

        self.stdout.write(self.style.SUCCESS('Successfully updated all video links'))