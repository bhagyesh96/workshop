from django.db import models



class Post(models.Model):
    text = models.CharField(max_length=200)
    title = models.TextField(null=True)
    cover = models.ImageField(upload_to='images/', default= '/images/Tiffiza.png', null=True, blank=True)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.title)


class PostDetail(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='pd')
    comment = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return str(self.post.title)
    
