from ..models import *

def findAll():
  return Product.objects.all()

def findById(id):
  return Product.objects.get(pk=id)