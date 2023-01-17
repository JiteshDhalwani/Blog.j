from django.db import models
from django.contrib.auth.models import User


# Create your models here.
CATEGORY_CHOICES = [
    ("Tech", "Tech"),
    ("Health", "Health"),
    ("Sports", "Sports"),
    ("Business", "Business"),
    ("Finance", "Finance"),
    ("None", "None")
]

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_written")
    title = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images', null=True)
    image_caption = models.TextField(null=True)
    readtime = models.CharField(max_length=64)
    category = models.CharField(
        max_length=64,
        choices=CATEGORY_CHOICES,
        default="None"
    )

    def __str__(self):
        return f"{self.id}. {self.title} written by {self.author}"
