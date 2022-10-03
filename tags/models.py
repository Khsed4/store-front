from django.db import models

from store.models import Product
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length = 255)


class TaggedItem(models.Model):
    tags = models.ForeignKey(Tag , on_delete = models.CASCADE)
#  a very poor way is to import the product straightly
# product = models.ForeignKey(Product)


# The other solution is to use the generic type 
# for using generic type we need to things:
#  Type: type of object like videos, products, items

#  ID: Id of the object which is gonna be used in relationship 
content_type = models.ForeignKey(ContentType, on_delete =models.CASCADE)
object_id = models.PositiveIntegerField()
content_object = GenericForeignKey()