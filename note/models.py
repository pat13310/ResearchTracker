from django.db import models
from authentication.models import CustomUser


class Note(models.Model):
    NOTE_TYPES = (
        ('text', 'Texte'),
        ('image', 'Image'),
        ('video', 'Vidéo'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True, null=True)
    note_type = models.CharField(max_length=10, choices=NOTE_TYPES, default='text')
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)
    video = models.FileField(upload_to='static/videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='static/uploads/', blank=True, null=True)

    def __str__(self):
        return self.title or "Note"

    def save(self, *args, **kwargs):
        # Ensure content is empty if the note is not of type 'text'
        if self.note_type != 'text':
            self.content = ''
        super().save(*args, **kwargs)
