from home.models import *

class Category(object):
    title = ''
    def getChild(_self):
        pass

class BookCategory(Category):
    title = 'Sách'
    def getChild(_self):
        return Theloaisach.objects.all()

class ElectroCategory(Category):
    title = 'Điện tử'
    def getChild(_self):
        return Theloaidientu.objects.all()

class ClotheCategory(Category):
    title = 'Quần áo'
    def getChild(_self):
        return Theloaiquanao.objects.all()

class CategoryFactory:
    availableCategories = ['book', 'electro', 'clothe']
    @staticmethod
    def getCategory(type) -> Category:
        if type.lower() not in CategoryFactory.availableCategories:
            return None
        targetclass = type.capitalize()
        return globals()[targetclass + 'Category']()