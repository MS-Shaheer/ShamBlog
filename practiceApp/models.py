from django.db import models
from django.utils.html import format_html
# from tinymce.models import HTMLField
# Create your models here.

#Category Model
class sportsCategory(models.Model):
    categoryID = models.AutoField(primary_key = True)
    sportsName = models.CharField(max_length = 30)
    description = models.TextField()
    urls = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = "sportsCategory/")
    addDate = models.DateTimeField(auto_now_add = True, null = True)

    def show_image(self):
        return format_html('<img src="/media/{}" style="width:50px; height:50px;" />'.format(self.image))
    
    def __str__(self):
        return self.sportsName

#Post Model
class sportsPost(models.Model):
    postID = models.AutoField(primary_key = True)
    postName = models.CharField(max_length = 50)
    content = models.TextField()
    urls = models.CharField(max_length = 100)
    category = models.ForeignKey(sportsCategory, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = "sportsPost/")

    def show_image(self):
        return format_html('<img src="/media/{}" style="width:50px; height:50px;" />'.format(self.image))
    
    def __str__(self):
        return self.postName
