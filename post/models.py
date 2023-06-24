from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='post_images', blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, related_name='posts')
    is_active = models.BooleanField(default=True)
    likes = models.ManyToManyField('users.User', related_name='likes', blank=True)
    total_likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f'{self.author.full_name} - {self.content[:20]}'


@receiver(m2m_changed, sender=Post.likes.through)
def post_likes_changed(sender, instance, **kwargs):
    instance.total_likes = instance.likes.count()
    instance.save()


class Like(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE)

    # count = models.IntegerField()
    # date_liked = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f'{self.user.full_name} - {self.post.content[:20]}'


class Favorite(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f'{self.user.full_name}'
