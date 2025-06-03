from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('education', 'Education & Learning'),
        ('technology', 'Technology'),
        ('health', 'Health'),
        ('finance', 'Finance'),
        ('entertainment', 'Entertainment'),
        ('travel', 'Travel'),
        ('personal_dev', 'Personal Development'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    abstract = models.TextField()
    content_file = models.FileField(upload_to='articles/content/')

    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
