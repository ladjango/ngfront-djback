from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    image = models.ImageField(upload_to='uploads/')
    category = models.ForeignKey('menu.Category')

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

