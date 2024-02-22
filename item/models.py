from django.db import models

# Create your models here.
class Item(models.Model):
    item_id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name