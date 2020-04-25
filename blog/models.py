from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)  #auto_now_add takes the exact time of creation
    author=models.ForeignKey(User,on_delete=models.CASCADE) #on delete is used if user is deleted , their posts will also get deleted on selecting models.Cascade

    def __str__(self):
        return self.title

    ''' redirect oly redirects to the path mentioned but reverse
        actually sends back the url of that path
    '''

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
