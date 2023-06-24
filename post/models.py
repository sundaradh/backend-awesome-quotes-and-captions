from django.db import models


class Post(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, related_name='posts')
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f'{self.author.full_name} - {self.content[:20]}'





