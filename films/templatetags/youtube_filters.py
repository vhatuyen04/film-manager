# your_app/templatetags/youtube_filters.py

from django import template
import re

register = template.Library()

@register.filter
def youtube_embed(value):
    """
    Converts a YouTube URL into an embeddable URL.
    """
    youtube_regex = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    match = re.match(youtube_regex, value)
    if match:
        video_id = match.group(6)
        return f'https://www.youtube.com/embed/{video_id}'
    return value


@register.simple_tag
def test_tag():
    return "Test tag loaded successfully!"