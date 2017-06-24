#encoding=utf-8
class Product:
    "product class（a base class）"
    def show_attr(self):
        pass


class Factory:
    "factory class（a base class）"
    def create_product(self):
        pass


class ProductA(Product):
    "a derived class of product class"
    def __init__(self,attr1,att2):
        self.attr1=attr1
        self.attr2=att2

    def show_attr(self):
        print self.attr1+self.attr2


class ProductB(Product):
    "a derived class of product class"
    def __init__(self,attr):
        self.attr=attr

    def show_attr(self):
        print self.attr*2


class FactoryA(Factory):
    "a derived class of factory class"
    def create_product(self,attr1,attr2):
        return ProductA(attr1,attr2)


class FactoryB(Factory):
    "a derived class of factory class"
    def create_product(self,attr):
        return ProductB(attr)


product_a=FactoryA().create_product('create ','product a')
product_a.show_attr()
product_b=FactoryB().create_product('product b ')
product_b.show_attr()