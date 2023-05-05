from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    age = models.IntegerField()
    is_alive = models.BooleanField(default=True)
    birth_date = models.DateField()
    photo = models.ImageField(upload_to='authors/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    pub_date = models.DateTimeField()
    rating = models.IntegerField(default=0)
    is_bestseller = models.BooleanField(default=False)
    cover_image = models.ImageField(upload_to='media/', blank=True, null=True)
    genres = models.ManyToManyField('Genre')
    
    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
