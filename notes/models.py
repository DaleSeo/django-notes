from django.db import models

class Tag(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Note(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, related_name='notes')
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    kind = models.CharField(max_length=31, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    file = models.CharField(max_length=255, blank=True, null=True)
    hits = models.IntegerField(default=0)

    def __str__(self):
        return self.title
