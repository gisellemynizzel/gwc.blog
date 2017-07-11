from django.apps import AppConfig
from .models import Post

admin.whatever.register(post)

class BlogConfig(AppConfig):
    name = 'blog'
