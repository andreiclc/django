import uuid
from django.db import models

class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_movie = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    rating = models.IntegerField()
    storyline = models.CharField(max_length=1000)
    release_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'movie'