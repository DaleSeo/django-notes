from django.db import models

class Note(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    memo = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
