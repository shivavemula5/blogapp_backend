from django.db import models
from accounts.models import UserAccount

class Post(models.Model):
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE,related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    time_required = models.IntegerField()

    def __str__(self):
        return f'{self.id} . {self.title}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE,related_name='comments')
    comment = models.TextField()
    class Meta:
        unique_together = ['user','post']

class LikedPosts(models.Model):
    liked = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='likedposts')
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE,related_name='likedposts')
    class Meta:
        unique_together = ['post','user']


class SavedPosts(models.Model):
    saved = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='savedposts')
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE,related_name='savedposts')
    class Meta:
        unique_together = ['post','user']

class MarkAsRead(models.Model):
    read = models.BooleanField(default=False)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='markasread')
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE,related_name='markasread')
    
class Tags(models.Model):
    tag = models.CharField(max_length=50)

class PostWithTags(models.Model): 
    tag = models.ForeignKey(Tags,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
