from django.db import models

class ProductPerson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class ProductDetails(models.Model):
    person = models.OneToOneField(ProductPerson, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField()
    
    def __str__(self):
        return str(self.person)
    class Meta:
        verbose_name_plural = "ProductDetails"
    